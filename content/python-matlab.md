Title: Comparing Python and Matlab for teaching in science
Date: 2017-11-08 12:00
Tags: Programming, education, open source, free software, Matlab, Python
Category: teaching
Slug: python-matlab
Author: Matthew Brett
Summary: Comparing Python and Matlab for Psychology teaching

# How easy are they to learn?

Python is a standard language for courses designed as an introduction to
computer programming.

Here is a quick survey of some major US Universities:

* Of the [MIT OpenCourseWare courses on general
  programming](https://ocw.mit.edu/courses/intro-programming/#general) four
  are in Python and one is in Java.
* MIT Electrical Engineering and Computer Science courses are [6.0001:
  Introduction to Computer Science and Programming in
  Python](https://www.eecs.mit.edu/academics-admissions/academic-information/subject-updates-ft-2014/60001)
  and [6.0002 Introduction to Computational Thinking and Data
  Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016),
  both in Python. MIT [switched to Python from
  Scheme](https://www.wisdomandwonder.com/link/2110/why-mit-switched-from-scheme-to-python).
  [Scheme](https://groups.csail.mit.edu/mac/projects/scheme) is a variant of
  the [Lisp programming
  language](https://en.wikipedia.org/wiki/Lisp_(programming_language)).
* Berkeley runs a large [cross-discipline undergraduate program on data
  science](http://data8.org) using Python.  There is a matching [Cognitive
  Science connector course]( http://data8.org/cognitive-science-connector).
  Their computer science [introduction to computer programming course -
  61A](http://www-inst.eecs.berkeley.edu/~cs61a/sp12/) uses Python.  Like MIT,
  Berkeley [switched to Python from
  Scheme](https://people.eecs.berkeley.edu/~bh/61a.html).  Another [more basic
  course - CS10](http://cs10.org/fa17) uses a variant of
  [Scratch](https://scratch.mit.edu), a visual programming language.
* [Stanford CS101: Introduction to Computing
  Principles](http://web.stanford.edu/class/cs101) uses a variant of
  JavaScript.
* [Harvard and Yale Introduction to Computer Science
  CS50](https://docs.cs50.net/2017/fall/syllabus/cs50.html) "Languages include
  C, Python, SQL, and JavaScript plus CSS and HTML".
* [Washington University Introduction to Programming
  I](https://courses.cs.washington.edu/courses/cse142) uses Java.
* [Caltech Introduction to Computer
  Programming](http://cms.caltech.edu/academics/course_desc#cs) uses Python.

Of the introductory programming courses run by Computer Science departments in
the UK Russell group, 12 teach Java as a first language, 4 teach Python, 4
teach C and 3 teach Haskell [^russell-teaches].

[^russell-teaches]: [Birmingham: Java](https://www.birmingham.ac.uk/undergraduate/courses/computer-science/computer-science.aspx);
    [Bristol: C, Haskell,
    Java](http://www.bristol.ac.uk/unit-programme-catalogue/RouteStructure.jsa?byCohort=N&ayrCode=18%2F19&programmeCode=4COSC006U);
    [Cambridge:
    Java](https://www.undergraduate.study.cam.ac.uk/courses/computer-science);
    [Cardiff:
    Python](https://www.cardiff.ac.uk/study/undergraduate/courses/2018/computer-science-bsc);
    [Durham:
    Java](https://www.dur.ac.uk/faculty.handbook/module_description/?year=2017&module_code=COMP1011);
    [Edinburgh: Haskell](http://www.drps.ed.ac.uk/17-18/dpt/cxinfr08013.htm);
    [Exeter:
    Python](https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comsci/#Programme-structure);
    [Glasgow:
    Python](https://www.gla.ac.uk/undergraduate/degrees/computingscience);
    [Imperial:
    Haskell](http://www.imperial.ac.uk/computing/current-students/courses/120_1/);
    [Kings:
    Java](https://www.kcl.ac.uk/nms/depts/informatics/study/current/handbook/Progs/Modules/4CCS1PPA.aspx);
    [Leeds:
    C](http://lib5.leeds.ac.uk/rlists/broker/?bbModuleId=201718_32439_COMP1711&bbListId=_5264080_1);
    [Liverpool:
    Java](http://readinglists.liverpool.ac.uk/modules/comp101.html); [LSE: No
    course](http://www.lse.ac.uk/study-at-lse/Undergraduate); [Manchester:
    Java](http://www.manchester.ac.uk/study/undergraduate/courses/2018/00560/bsc-computer-science/course-details/#course-profile);
    [Newcastle:
    Java](https://eu01.alma.exlibrisgroup.com/leganto/readinglist/searchlists/3360129130002411);
    [Nottingham: C, Java,
    Haskell](http://readinglists.nottingham.ac.uk/lists/874C6774-DEBE-E92D-E806-41E591A49A30.html);
    [Oxford:
    Haskell](http://www.cs.ox.ac.uk/admissions/undergraduate/courses/computer_science_core_1.html#Functional_Programming),
    [Oxford:
    Scala](https://www.cs.ox.ac.uk/teaching/courses/2017-2018/imperativeprogramming1/index.html);
    [Queen Mary:
    Java](http://www.eecs.qmul.ac.uk/undergraduates/programme/view/38);
    [Queen's Belfast: Java](https://github.com/thomaspickup/qub-yr1-java);
    [Sheffield:
    Java](https://www.sheffield.ac.uk/prospectus/courseDetails.do?id=G4022018);
    [Southampton:
    Java](https://www.southampton.ac.uk/courses/modules/comp1202.page#_ga=2.46435175.1162187456.1510165927-1517032892.1510165927);
    [UCL: C,
    Haskell](http://readinglists.ucl.ac.uk/lists/15F03E6E-6D5F-7073-B7C6-BBF5C86E83C5.html);
    [Warwick:
    Java](https://www2.warwick.ac.uk/fac/sci/dcs/teaching/modules/cs118/);
    [York:
    Python](https://www.york.ac.uk/students/studying/manage/programmes/module-catalogue/module/COM00007C/2017-18).

Common languages other than Python in introductory programming courses are
Java, C, and Haskell.  Neither Java nor Haskell are widely used in psychology
or scientific programming.  C has a niche use for system programming and speed
optimization, but it is a bad choice for the kind high-level programming that
most scientists use for their work.

I don't know of any university where their main introduction to programming
course uses Matlab. One reason may be the opinions shown in this [survey of
computing
languages](https://plus.google.com/u/0/+MatthewBrett/posts/HAsy7HWMyc5).
Sadly the [source site](http://hammerprinciple.com/therighttool) had gone down
at the time I wrote this, but the [Archive.org
copy](https://web.archive.org/web/20170204183750/hammerprinciple.com/therighttool)
has pages summarizing
[Python](https://web.archive.org/web/20170205052954/http://www.hammerprinciple.com:80/therighttool/items/python)
and
[Matlab](https://web.archive.org/web/20170205074106/http://www.hammerprinciple.com:80/therighttool/items/matlab).
Abstracting from my earlier summary: the survey responses suggest that Matlab
is a niche language, and is harder to learn than Python.  Matlab code is less
elegant, less readable, harder to maintain and harder to re-use.

In particular, Matlab rates much higher than Python on the question "This
language is unusually bad for beginners", "This language has an annoying
syntax" and "Writing code in this language is a lot of work".

Computer science departments often choose the language for the lessons it can
teach about how programming languages work, rather than their general use for
doing real work.  The fact that institutions like Berkeley and MIT are
switching to Python from other languages suggests that Python has enough range
to cover both domains (see below).

# Number of users

* [Popularity of Programming Languages](http://pypl.github.io/PYPL.html): "The
  PYPL PopularitY of Programming Language Index is created by analyzing how
  often language tutorials are searched on Google.".  October 2017 - Python
  second at 17.6% (after Java); Matlab 11th on 2.2%.
* [TIOBE index](https://www.tiobe.com/tiobe-index): "The ratings are based on
  the number of skilled engineers world-wide, courses and third party vendors.
  Popular search engines such as Google, Bing, Yahoo!, Wikipedia, Amazon,
  YouTube and Baidu are used to calculate the ratings.".  Python 5th (after
  Java, C, C++, C#) at 3.9%.  Matlab 13th at 1.9%.

# Trends

* [The Incredible Growth of
  Python](https://stackoverflow.blog/2017/09/06/incredible-growth-python):
  analysis of StackOverflow search trends in high-income nations.  Python was
  the most visited tag of any language in June 2017, at around 10%, and has
  had 27% growth from 2016 to 2017, with a linear trend since 2012.  In
  contrast, Matlab was at 0.4% and had about an 18% drop from 2016 to 2017.
  Much of the growth of Python is in "data science" searches.

# Range

* Data analysis: Python >> Matlab.  Matlab is not a serious contender in data
  science. The [StackOverflow data science search
  tag statistics](https://datascience.stackexchange.com/tags) show
  machine-learning as the top tag with 2173 questions, Python is second with
  945 and Matlab is 52nd with 60 questions.
* Statistics: Python ~= Matlab.  Both have deficiencies.  Python has the major
  machine learning toolbox.
* Real-time programming: Python == Matlab ?
  ([Psychopy](http://www.psychopy.org/) ==
  [Psychtoolbox](http://psychtoolbox.org/) - they both claim roughly around
  12K active users: [Psychopy users](http://www.psychopy.org/usage.php),
  [Psychtoolbox Wikipedia
  page](https://en.wikipedia.org/wiki/Psychtoolbox_for_MATLAB));
* Shell scripting: Python >> Matlab;
* Tutorial and demo development: Python > Matlab (Jupyter Notebook);

For example, for a course on brain imaging, students should be able to:

1. write simple command line scripts for handling files and directories;
2. script their analyses in FSL and other packages;
3. present stimuli for experiments;

Matlab is not a good choice for the first two tasks.

# Convenience, access, transfer

Matlab has a fairly convenient installer, but there are similar installers for
Python - such as the [Anaconda Python Installer](https://anaconda.org).

Unlike Matlab, Python and all its standard packages are available for free, so
a student can install a full copy on any machine they want, and they can take
their installation to their next lab or next job without worrying about Matlab
license fees.

Using Python makes it easier to collaborate with researchers in universities
that cannot afford or will not pay for Matlab licenses.

# Culture

Python is open-source.  This may be the reason for the following features of
its community:

* strong culture of testing and quality;
* well-developed packaging;
* tradition of users becoming contributors.

# Employability

Python programming is a desirable skill in industry; [Stackoverflow Jobs:
Python](https://stackoverflow.com/jobs?sort=i&q=Python) currently gives 721
hits, [Stackoverflow Jobs:
Matlab](https://stackoverflow.com/jobs?sort=i&q=Matlab) gives 36.

# Moving from Matlab to Python

See [this excellent white
paper](https://www.enthought.com/wp-content/uploads/Enthought-MATLAB-to-Python-White-Paper.pdf).

Most scientific users of Python install the following Python packages:

* [Numpy](https://en.wikipedia.org/wiki/NumPy) (array manipulation);
* [Scipy](https://en.wikipedia.org/wiki/SciPy) (scientific toolbox, including
  sparse arrays, optimization).
* [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib) (2D and some basic 3D
  plotting);
* [IPython](https://en.wikipedia.org/wiki/IPython) / [Jupyter
  Notebook](https://jupyter.org) (interactive console and web application).

For example, the [Anaconda installer](https://anaconda.org) installs Python,
these packages, and many more.

These packages together give you a rough equivalent to a standard Matlab
installation with some toolboxes installed.

There is no direct Python equivalent of the Simulink application - see
[Simulink alternatives](http://www.walkingrandomly.com/?p=4379).
