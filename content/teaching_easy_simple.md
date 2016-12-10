Title: Teaching easy, teaching simple
Date: 2016-12-09 12:00
Tags: Thinking, Teaching, Coding
Category: teaching
Slug: teaching-simple
Author: Matthew Brett
Summary: We should teach for the long term using simple tools

## Easy and simple

I am going to use the definitions of "simple" and "easy" from [this
talk](http://www.infoq.com/presentations/Simple-Made-Easy).

* Simple comes from Latin *simplex* - one fold.  Simple is the opposite of
  *complex*, which comes from the Latin for "twisted together".
* Easy comes from old French *aiser* which in turn comes from the Latin
  *adjacens* "lying close by" ([^oxford-dictionary])

[^oxford-dictionary]: Oxford dictionary of Word origins edited by Julia
Cresswell.

"Easy" is what you are familiar with. "Easy" is not far from something you
already know.

"Simple" is when you have succeeded in breaking the problem into separate
component ideas.

## Easy tools, simple tools

I use a general-purpose text editor for as many tasks as I can.  For the last
six years I have used Vim and Gvim; before that, I used Emacs.  Like many
powerful text editors, Vim and Emacs can be configured for editing many
different types of text files, including code in different languages.   For
example, I am using Vim to edit this text in Markdown format; Vim does
Markdown syntax highlighting.

I had been using Emacs in this way for a long time before I read this advice
in the classic book "The Pragmatic Programmer" by Andrew Hunt and David Thomas
(2000):

> *Use a Single Editor Well*
>
> The editor should be an extension of your hand; make sure your editor is
> configurable, extensible, and programmable.

When I have a task that needs thought, I often sketch the code or text on a
piece of paper, then fill out the sketch in Vim.  For example, I wrote the
first draft of this post in an art notebook with large pages, and now I am
typing it up and editing in Vim.

I use Vim to read and write:

* code in Python, C and MATLAB;
* papers or reference letters using LaTeX;
* tutorials in Restructured Text;
* presentations in Markdown / LaTeX;

To execute code I use the terminal command line, or the IPython Python
interpreter, which is also a terminal application.  I use command-line tools
like `make` to build my papers and presentations.  In the days when I used
MATLAB daily, I preferred to start it in `-nodesktop` mode, to disable most of
the graphical user interface.

Very occasionally I use a specialized tool for a short task that does not need
much thought.   For example I sometimes use LibreOffice or OSX Pages to write
short letters, Keynote for a presentation with many graphics, or the Jupyter
notebook when I am experimenting with plots in Python, or when I am writing a
demonstration of code I already understand.

As soon as the task needs some thought, I switch into my text editor. I do
this to relieve myself of the burden of using the richer and more complicated
interfaces of the other tools.  I am very familiar with my text editor, so I
no longer have to think how to do things like editing text.  With Vim, in
particular, I find that the cursor seems to follow my eyes; I have little or
no conscious sensation of what my hands are typing as they enter the commands
to move the cursor.

I am sure I am not alone in finding it hard to think clearly.  If you give me
an interface that makes it easy to play with code in a sloppy and unstructured
way, I will.  Sometimes doing that is useful, but most of the time, giving in
to the temptation to play with code is disastrous for my clarity of thought.

I think more clearly in Vim because I have used Vim enough that my hands and
my motor cortex can do the mechanical work of editing, leaving the rest of my
brain free for thinking ([^two-paths]).  I do not have to interrupt my
concentration by moving my hands to the mouse or trackpad, because I can do
everything I need with the keyboard commands.  Using my text editor is simple,
because the task of editing is not entangled with the task of thinking.

[^two-paths]: there is good neuroscientific evidence for this simple
distinction between habitual tasks and tasks that require conscious effort.
If you try and do two tasks that require conscious effort, they interfere with
one another so you cannot do both tasks well.  If you do an habitual task at
the same time as a task that requires conscious effort, the tasks interfere
much less.

## Easy and simple in teaching

When we teach scientists to write and use code, new students are unlikely to
know a general-purpose text editor well, and may never have used a terminal
application.  It does not seem practical for them to learn to use an editor
and the terminal as well as the other new things we teach.  For that reason,
many courses give students an easy interactive environment such as the MATLAB
workspace, R Studio or the Jupyter Notebook.  The idea is that it makes it
easier for the students to concentrate on code rather than learning how to use
the tools.  In my experience, the students often continue using the easy tools
from the class, and do not go on to learn the simple tools that experts use.

Some teachers do not believe that their students should be using the same
tools as the experts.  The argument is that scientists use and write code in a
different way from programmers, so they do not need the tools that a
programmer would choose.  If that argument were correct, that would be happy
for teachers, because the simple tools are hard to teach.

I chose my tools to help me think clearly.  Does a scientist using code need
less clarity of thought than a programmer?  Your answer to this will probably
depend on your model of scientific practice.  If you think that a scientist
should spend most of their time exploring code and data in an informal way,
you might conclude that "easy" is acceptable, even desirable.  My own
experience of using tools like the Jupyter Notebook is that I cannot afford to
work in this way without exposing myself to great risk from ubiquitous error
and self-deception ([^ubiquitous-error]).  If your experience of science is
like mine, you will probably prefer "simple".

[^ubiquitous-error]: "The scientific method's central motivation is the
ubiquity of error - the awareness that mistakes and self-delusion can creep in
absolutely anywhere and that the scientist's effort is primarily expended in
recognizing and rooting out error" David L. Donoho *et al* (2009)
"Reproducible research in computational harmonic analysis" Computing in
Science & Engineering 11 p8-18.

You might accept that scientists do need to learn the simple tools at some
point, but the constraints of your course do not allow you to spend time on
teaching tools.  Teaching the simple tools, would take too long.  In that case
you have to consider the potential for damage to the students' practice over
the long term.  If a student sees their teachers using easy tools, and
encouraging them to do the same, they are less likely to commit themselves to
the hard work necessary to learn the simple tools.  To quote a friend and
colleague: "It would be terrible if we make a generation of copy-paste
scientists".

As I have taught more, I have put more effort into introducing students to the
simple tools right at the beginning of my course.  I want to teach students
tools that I would use myself.  We use the terminal to run bash and git
commands, the IPython console for exploring small code fragments, and a
full-featured text editor for editing code and documents.  In my [most recent
course](https://bic-berkeley.github.io/psych-214-fall-2016) we used the Atom
text editor. Sometimes I do use the Jupyter Notebook for my own work, bit I am
careful not to use it in class, because it is so addictive, and therefore
dangerous for an inexperienced user of code.

## Teach simple, not easy

Teaching always involves some degree of instruction that is implicit.  The
students take our working practice as a model of expertise.  This model can be
more more persuasive than anything else we teach.  We should use implicit and
explicit learning to teach effective practice.  Sound working practice is
the foundation on which we build; it is worth the cost in curriculum time to
s]how the benefit of simple, and the risks of easy.
