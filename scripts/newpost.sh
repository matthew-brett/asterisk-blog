#!/bin/bash
PEDITOR=${POST_EDITOR:-${GUI_EDITOR-${EDITOR}}}
slug=$(python scripts/make_post.py "$NAME")
$PEDITOR "$slug"
