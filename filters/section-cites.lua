--[[
  section-cites.lua

  Auto-id headings for configured works (AH, IF, …) and rewrite
  @ah-3-vi-3 / @if-ii Cite nodes into links (optionally cross-page via
  works.<key>.target).

  Run before citeproc (Quarto: filters at: pre-quarto).
]]

local conf = {
  works = {},
  id_prefix = "sec",
  auto_id = true,
}

local used_ids = {}

local function stringify(x)
  return pandoc.utils.stringify(x or "")
end

local function setup(meta)
  local sc = meta["section-cites"]
  if not sc then
    return
  end
  if sc["id-prefix"] then
    conf.id_prefix = stringify(sc["id-prefix"])
  end
  if sc["auto-id-headings"] ~= nil then
    local v = sc["auto-id-headings"]
    if type(v) == "boolean" then
      conf.auto_id = v
    else
      conf.auto_id = stringify(v) ~= "false"
    end
  end
  if not sc.works then
    return
  end
  conf.works = {}
  for key, spec in pairs(sc.works) do
    local k = tostring(key):lower()
    local entry = {
      label = k:upper(),
      names = { preface = true },
      target = "",
      -- "book-chap-sect" (AH) vs "number" (IF)
      scheme = "cite",
    }
    local st = pandoc.utils.type(spec)
    if st == "table" or st == "MetaMap" then
      if spec.label then
        entry.label = stringify(spec.label)
      end
      if spec.target then
        entry.target = stringify(spec.target):gsub("/$", "")
      end
      if spec.scheme then
        entry.scheme = stringify(spec.scheme)
      end
      if spec.names then
        local nt = pandoc.utils.type(spec.names)
        if nt == "List" or nt == "MetaList" then
          for _, n in ipairs(spec.names) do
            entry.names[stringify(n):lower()] = true
          end
        end
      end
    else
      entry.label = stringify(spec)
    end
    conf.works[k] = entry
  end
end

local function is_named(work, chap)
  local w = conf.works[work]
  return w and w.names[chap:lower()]
end

local function format_chapter(work, chap)
  if is_named(work, chap) then
    local s = chap:lower()
    return s:sub(1, 1):upper() .. s:sub(2)
  end
  return chap:upper()
end

local function make_id_cite(work, book, chap, sect)
  local id = string.format(
    "%s-%s-%s-%s",
    conf.id_prefix,
    work,
    book,
    chap:lower()
  )
  if sect and sect ~= "" then
    id = id .. "-" .. sect:lower()
  end
  return id
end

local function make_id_number(work, n)
  return string.format("%s-%s-%s", conf.id_prefix, work, tostring(n):lower())
end

local function format_number(n)
  -- Roberts fragment labels are Roman numerals; keep arabic as-is.
  if tostring(n):match("^[ivxlcdmIVXLCDM]+$") then
    return tostring(n):upper()
  end
  return tostring(n)
end

local function unique_id(base)
  if not used_ids[base] then
    used_ids[base] = 1
    return base
  end
  used_ids[base] = used_ids[base] + 1
  return base .. "-" .. tostring(used_ids[base])
end

local function claim_id(id)
  used_ids[id] = (used_ids[id] or 0) + 1
end

-- AH 3, VI:3 / AH 1, Preface:1 / AH 3, Preface
local function parse_heading_cite(text, label)
  local pat = "^"
    .. label
    .. "%s*(%d+)%s*,%s*([A-Za-z]+)%s*:?%s*([%w%-]*)"
  local book, chap, sect = text:match(pat)
  if not book then
    return nil
  end
  if sect == "" then
    sect = nil
  end
  return book, chap, sect
end

-- IF II / IF XXXI: Letter to Florinus (Roberts Roman numeral, or arabic)
local function parse_heading_number(text, label)
  local n = text:match("^" .. label .. "%s*([IVXLCDMivxlcdm]+)%s*:?")
  if not n then
    n = text:match("^" .. label .. "%s*(%d+)%s*:?")
  end
  if not n then
    return nil
  end
  return n
end

local function parse_cite_id(cid)
  -- if-ii / if-xxxi / if-1
  local work, n = cid:match("^([%a]+)%-([ivxlcdmIVXLCDM]+)$")
  if not work then
    work, n = cid:match("^([%a]+)%-(%d+)$")
  end
  if work then
    work = work:lower()
    local w = conf.works[work]
    if w and w.scheme == "number" then
      return { scheme = "number", work = work, n = n }
    end
  end
  -- ah-3-vi-3 / ah-1-preface-1
  local work, book, chap, sect =
    cid:match("^([%a]+)%-(%d+)%-([%a]+)%-([%w%-]+)$")
  if work then
    work = work:lower()
    if conf.works[work] then
      return {
        scheme = "cite",
        work = work,
        book = book,
        chap = chap,
        sect = sect,
      }
    end
  end
  -- ah-3-preface (no section)
  work, book, chap = cid:match("^([%a]+)%-(%d+)%-([%a]+)$")
  if work then
    work = work:lower()
    if conf.works[work] then
      return {
        scheme = "cite",
        work = work,
        book = book,
        chap = chap,
        sect = nil,
      }
    end
  end
  return nil
end

local function pretty(parts)
  local w = conf.works[parts.work]
  if parts.scheme == "number" then
    return string.format("%s %s", w.label, format_number(parts.n))
  end
  local c = format_chapter(parts.work, parts.chap)
  if parts.sect then
    return string.format("%s %s, %s:%s", w.label, parts.book, c, parts.sect)
  end
  return string.format("%s %s, %s", w.label, parts.book, c)
end

local function id_for(parts)
  if parts.scheme == "number" then
    return make_id_number(parts.work, parts.n)
  end
  return make_id_cite(parts.work, parts.book, parts.chap, parts.sect)
end

local function href_for(work, id)
  local target = conf.works[work].target
  if target and target ~= "" then
    return target .. "/#" .. id
  end
  return "#" .. id
end

local function our_id(id)
  if not id or id == "" then
    return false
  end
  local work = id:match("^" .. conf.id_prefix .. "%-([%a]+)%-")
  return work and conf.works[work:lower()] ~= nil
end

local function assign_header_id(el)
  if not conf.auto_id then
    return el
  end
  local title = stringify(el.content)
  for key, entry in pairs(conf.works) do
    if entry.scheme == "number" then
      local n = parse_heading_number(title, entry.label)
      if n then
        if our_id(el.identifier) then
          claim_id(el.identifier)
        else
          el.identifier = unique_id(make_id_number(key, n))
        end
        return el
      end
    else
      local book, chap, sect = parse_heading_cite(title, entry.label)
      if book then
        if our_id(el.identifier) then
          claim_id(el.identifier)
        else
          el.identifier = unique_id(make_id_cite(key, book, chap, sect))
        end
        return el
      end
    end
  end
  if el.identifier ~= "" then
    claim_id(el.identifier)
  end
  return el
end

local function rewrite_cite(el)
  if next(conf.works) == nil or #el.citations == 0 then
    return nil
  end
  local parts_list = {}
  for _, c in ipairs(el.citations) do
    local p = parse_cite_id(c.id)
    if not p then
      return nil
    end
    table.insert(parts_list, p)
  end
  if #parts_list == 1 then
    local p = parts_list[1]
    local id = id_for(p)
    return pandoc.Link({ pandoc.Str(pretty(p)) }, href_for(p.work, id))
  end
  local inlines = {}
  for i, p in ipairs(parts_list) do
    if i > 1 then
      table.insert(inlines, pandoc.Str("; "))
    end
    local id = id_for(p)
    table.insert(
      inlines,
      pandoc.Link({ pandoc.Str(pretty(p)) }, href_for(p.work, id))
    )
  end
  return inlines
end

local function rewrite_span(el)
  local work = nil
  for _, class in ipairs(el.classes) do
    local key = class:match("^([%w]+)%-section$")
    if key and conf.works[key:lower()] then
      work = key:lower()
      break
    end
  end
  if not work then
    return nil
  end
  local entry = conf.works[work]
  local text = stringify(el.content)
  local parts
  if entry.scheme == "number" then
    local n = parse_heading_number(text, entry.label)
    if not n then
      return nil
    end
    parts = { scheme = "number", work = work, n = n }
  else
    local book, chap, sect = parse_heading_cite(text, entry.label)
    if not book then
      return nil
    end
    parts = {
      scheme = "cite",
      work = work,
      book = book,
      chap = chap,
      sect = sect,
    }
  end
  return pandoc.Link(el.content, href_for(work, id_for(parts)), "", el.attr)
end

-- Two-pass: claim explicit our-ids first, then assign / rewrite.
function Pandoc(doc)
  if next(conf.works) == nil then
    return nil
  end
  used_ids = {}
  local function walk_headers(blocks, claim_only)
    for i, b in ipairs(blocks) do
      if b.t == "Header" then
        if claim_only then
          if our_id(b.identifier) then
            claim_id(b.identifier)
          end
        else
          blocks[i] = assign_header_id(b)
        end
      elseif b.content and (b.t == "BlockQuote" or b.t == "Div") then
        walk_headers(b.content, claim_only)
      end
    end
  end
  walk_headers(doc.blocks, true)
  walk_headers(doc.blocks, false)
  return doc:walk({ Cite = rewrite_cite, Span = rewrite_span })
end

return {
  { Meta = setup },
  { Pandoc = Pandoc },
}
