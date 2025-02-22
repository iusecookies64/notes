### Introduction

Look at the program below, it is written in **Jack** programming language, which is something that we are going to develop in this course. This is usually the first program that a student taking CS course write i.e. the **Hello World!** program.

```Jack
class Main {
	function void main() {
		do Output.printString("Hello World!");
		do Output.printIn(); // new line
		return;
	}
}
```

When a programmer is writing such a program, it is almost never concerned how this program will actually run on the hardware, all it cares is what this program.

There is nothing bad about this way of programming, because there are enough problems to solve when developing an application, that if the programmer starts worrying about the low level details also, then they will simply go nuts.

Hence, developers live on multiple layers of abstraction, some of them are listed below,
- How the program is executed,
- How does writing on screen works,
- How does features like class, functions work,
- How does do, while etc loops work,
- How does the control of flow is given to functions and how does return work,
- How do the program uses the services of an operating system
- ... and many more

The fact that high level programmers don't have to worry about these low level details is a virtue. But someone has to worry about this, the different layers of abstraction that power any modern high level programming language are,
- Assembler
- Virtual Machine
- Compiler
- Operating System

Lets take a look at how our high level code gets translated and machine code, from where it could be run on the computer,

![[Pasted image 20250216225557.png]]

We have already built assembler and in this course we are going to build the remaining pieces i.e. the **Compiler** and **VM translator**.