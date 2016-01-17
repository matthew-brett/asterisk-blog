Title: Why do researchers write sloppy code?
Date: 2016-01-15 14:00
Tags: Thinking, Teaching, Coding
Category: teaching
Slug: love-letter
Author: Matthew Brett
Summary: A love letter to the computer

A friend of mine teaches a subject that involves scientific programming.  He
has several times told me that he is surprised at some of the work that
students turn in.  He tells me that it is often messy and badly written.
Despite his clear instructions, the code often does not run as written and may
have very obvious syntax errors, commented out lines for debugging and other
work-in-progress cruft.  He wonders why the students turn in such bad code,
when they would be much more careful turning in a mathematical proof.

This reminds me of a quote that I read a long time since, and have just found
again in the famous "Code Complete" ([^code-complete]).

[^code-complete]: Steve McConnell "Code Complete, second edition" (2004) p842.
Microsoft Press.

> In the early years of programming, a program was regarded as the private
> property of the programmer. One would no more think of reading a colleague's
> program unbidden than of picking up a love letter and reading it. This is
> essentially what a program was, a love letter from the programmer to the
> hardware, full of the intimate details known only to partners in an affair.
> Consequently, programs became larded with the pet names and verbal shorthand
> so popular with lovers who live in the blissful abstraction that assumes
> that theirs is the only existence in the universe. Such programs are
> unintelligible to those outside the partnership.

(Attributed to Michael Marcotty).

Students producing proofs in math have had a lot of practice in making the
proof easy to follow.  They know that the proof is for the teacher or grader,
and they write the proof for them.

Students do not have the same feeling about code.  For them, code is a private
conversation between them and the computer.  If the computer does what we
want, at least once, then the conversation that led to up that is outside the
scope of public comment. The fact that the computer did what we wanted is the
equivalent of the mathematical proof, and the code that made that happen is
equivalent to the working notes for the proof.

That way of thinking is surprising to someone who has spent time developing
software, because we know that we make many mistakes, and that, to reduce the
number of mistakes, we need to lay out our reasoning in code, for others to
check.

One difference between the developer and the student is that the developer
knows that their code has to give the right answer in a range of
circumstances, over a fairly long period of time, and on different types of
computers.  To defend ourselves, we ask "is this code correct?".  If we want a
good answer to this question, we have to write code that others can follow and
criticize. The student usually has a different task, which is to get the
computer to give a small number of required outputs.  Their question is "does
this code give the required outputs in the situations for which I will be
graded".  For that question, code quality is irrelevant.

That is a damn shame, because in due course, the student may go on to do
research.  Their work will very likely involve some kind of coding.  They have
learned that the point of coding is to get the desired result.  They write
terrible, poorly organized code, that is full of errors, hard to read, and
dangerous to re-use.  After some editing, the code produces a plausible
answer, but it is likely to be wrong, because, as every experienced coder
knows, [coders make errors all the
time](http://blog.nipy.org/ubiquity-of-error.html).  The researcher can only
know the answer is wrong if they know the code is wrong, but that is something
that they have no instinct to investigate.
