Title: Python and Matlab
Date: 2017-11-08 12:00
Tags: Programming, education, open source, free software, Matlab, Python
Category: teaching
Slug: python-matlab
Author: Matthew Brett
Summary: Comparing Python and Matlab for Psychology teaching

# How easy are they to learn?

Python is a standard language for first programming courses in:

* Of the [MIT courses on general
  programming](https://ocw.mit.edu/courses/intro-programming/#general) four
  are in Python and one is in Java.
* 

* [Result from survey of computing
  languages](https://plus.google.com/u/0/+MatthewBrett/posts/HAsy7HWMyc5).
  Sadly the [source
  site](http://hammerprinciple.com/therighttool) had gone down at the time I
  wrote this, but the [Archive.org copy](
  (https://web.archive.org/web/20170204183750/hammerprinciple.com/therighttool)
  has pages summarizing
  [Python](https://web.archive.org/web/20170205052954/http://www.hammerprinciple.com:80/therighttool/items/python)
  and
  [Matlab](https://web.archive.org/web/20170205074106/http://www.hammerprinciple.com:80/therighttool/items/matlab).
  Abstracting from my earlier summary: the survey responses suggest that
  Matlab is a niche language, and is harder to learn than Python.  Matlab code
  is less elegant, less readable, harder to maintain and harder to re-use.

  In particular, Matlab rates much higher than Python on the question "This
  language is unusually bad for beginners", "This language has an annoying
  syntax" and "Writing code in this language is a lot of work".

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
  science - see [StackOverflow data science search
  tags](https://datascience.stackexchange.com/tags).  Machine-learning is the
  top tag with 2173 questions, Python is second with 945 and Matlab is 52nd
  with 60 questions.
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

For an Imaging Course, students should be able to:

1. write simple command line scripts for handling files and directories;
2. script their analyses in FSL and other packages;
3. present stimuli for experiments;

Matlab isn't a good choice for the first two tasks.

# Convenience

* [Anaconda Python Installer](https://anaconda.org);
* Python has no license manager.

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
