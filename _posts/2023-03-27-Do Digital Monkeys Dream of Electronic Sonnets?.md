---
layout: distill
title: Do Digital Monkeys Dream of Electronic Sonnets?
description: The curious birth of information from randomness
tags: Information-Theory Statistical-Mechanics Computer-Simulation
giscus_comments: true
date: 2023-02-03
img: assets/img/Monkeys/Shakespeare_monkey.jpg
og_image: assets/img/Monkeys/Shakespeare_monkey.jpg
bibliography: 2023-03-27-Do_Digital_Monkeys_Dream_of_Electronic_Sonnets.bib

authors:
  - name: Roberto A. Gambarini
    affiliations:
      name: Imperial College London

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: What is Information?
  - name: The Infinitely Small Possibilities
  - name: Down to Monkey Business
  - name: All the World's a Monkey's Stage
  - name: Where art thou my Entropy?

# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }

---

## What is Information?

We encounter information in various forms, such as data entries on an Excel sheet, news reports, or social media posts. This information can be straightforward or intricate, based on facts or personal opinions, and can be either true or false. Information is the currency we use to exchange knowledge, and as the saying goes, knowledge is power. Information serves as the raw material that powers our understanding.
{: style="text-align: justify;"}

> What is the mathematical value of information?

Information theory is a field of applied mathematics that focuses on how we measure, store, and communicate information. <d-cite key="cover1999elements"></d-cite> It helps us answer fundamental questions about how information works. The science of information theory was born from the groundbreaking work of pioneering scientists like Claude Shannon, John von Neumann, and Alan Turing in the 20th century. <d-cite key="shannon1948mathematical"></d-cite> <d-cite key="von1956probabilistic"></d-cite> <d-cite key="turing2014enigma"></d-cite> These scientists created laws to regulate how we transmit, compress, decompress, and handle errors in information. <d-cite key="wicker1994error"></d-cite> To measure information, they decided to use bits, which are short for binary digits. <d-cite key="nyquist1924certain"></d-cite> Binary digits represent only two fundamental values, 0 and 1, and are crucial to electronic circuits' basic structure. These digits can help us distinguish between two states, such as high and low voltage levels, which can represent the two binary states of 0 and 1. <d-cite key="seggelmann2011strategies"></d-cite>
{: style="text-align: justify;"}

$$1 \qquad \qquad 0$$

$$Yes \qquad \quad No$$

$$True \quad \quad False$$

$$. \qquad \qquad -$$

$$\uparrow \qquad \qquad \downarrow$$

$$\leftarrow \qquad \qquad \rightarrow$$

<div class="caption">
    Binary numbers can be used in different ways. Such as expressing directions, simple answers, and even as an alternative representation of morse code.
</div>

This standard was not decided haphazardly. The binary values of 1 and 0 could be used had a wide variety of uses such as simple logical operations, and it is this versatility that allowed computers to tackle a wide array of problems <d-cite key="ralston1993encyclopedia"></d-cite>.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/Information_art.png"%}

In the fields of physics and cosmology, information has become a crucial tool to explore the underlying principles of the universe. <d-cite key="aaronson201612"></d-cite> Physicists use the 'bit' as the most fundamental building block that can be defined. <d-cite key="lloyd2002computational"></d-cite> Some physicists have proposed that the universe itself may operate like a giant computer, processing vast amounts of information through physical processes. <d-cite key="lloyd2002computational"></d-cite> The recent debate around Hawking radiation exemplifies the importance of information in physics. Hawking radiation suggests that black holes emit particles, which carry away information about the black hole's internal state. <d-cite key="hawking1976breakdown"></d-cite> One could argue that information theory represents the study of the very foundations of nature. <d-cite key="aaronson201612"></d-cite>
{: style="text-align: justify;"}

***

## The Infinitely Small Possibilities

The infinite monkey theorem is a popular thought experiment that shows the reality of minuscule probabilities. It considers the possibility that if you had a monkey use a typewriter, and the monkey could hit random keys for an infinite amount of time, that eventually he would eventually create a perfect copy of William Shakespeare's complete works. <d-cite key="gowers2008princeton"></d-cite> Mind you, there is nothing special about The Bard's timeless works. The same could be said about any text that ever existed. The floor in this monkey's room might as well be filled with every text ever conceived, every book that will be eventually written, and even your sunday shopping list. This certainly doesn't seem realistic does it? And it is not. At least not in this universe.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/roomFullofPapers.png"%}

For now, infinity remains a mathematical concept, far removed from the reality of physics. <d-cite key="brouwer1975intuitionism"></d-cite> Even though the probability of a monkey typing a Shakespearean sonnet correctly is infinitesimally small, games of chance offer better examples of this idea. For instance, the US Powerball is one of the most famous lottery games worldwide. Considering that it holds the record for the largest prize ever awarded in lottery, who wouldn't want to have the prize winning numbers? <d-cite key="grote2013economics"></d-cite> The game is as follows:
{: style="text-align: justify;"}

In the [US Powerball lottery](https://www.flalottery.com/exptkt/pwrball-odds.pdf), five balls are chosen at random from a pool of 69 numbered balls. Additionally, one red Powerball is chosen from a set of 26 numbered balls. If you correctly guess some of the numbers, you can win a portion of the prize money. However, you need to guess all the numbers in the correct order to win the grand prize.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/powerball.png"%}

<div class="caption">
    A simple representation of how the lottery numbers are drawn. Each white ball is uniquely numbered from 1 to 69 and each red Powerball is uniquely numbered from 1 to 26. During the picking, a mechanism will propel one of the balls outside of the box to ensure a random pick. Lovely lady announcing the numbers not included
</div>

How likely are you to win the jackpot? First let's consider the total number of possible combinations that might occur in this game. Combinatorics is a branch of mathematics that deals with the study of counting and arranging objects or elements. In this case we only care about how many different $$r$$ arrangements we can get from $$n$$. When $$r = 5$$ and $$n = 69$$ the solution is as follows:
{: style="text-align: justify;"}

$$C(r,n) = \frac{n!}{r!(n-r)!} = \frac{69!}{5!(69-5)!} = \frac{69 \times 68 \times 67 ... \times 1}{5 \times 4 ... \times 1 \times 64 \times 63 ... \times 1} = 11,238,513$$

<div class="caption">
    Reminder that the factorial of a number would be a series of operations in a number is multiplied by by the same number minus one until its multiplied by 1 $$a! = a \times (a - 1) \times ... \times 1 $$
</div>

For the single red Powerball it is as simple as:
{: style="text-align: justify;"}

$$C(r,n) = \frac{n!}{r!(n-r)!} = \frac{26!}{1!(26-1)!} = \frac{26 \times 25!}{1 \times 25!} = 26$$

So we are left to choose between $$11,238,513$$ (known as $$N$$) possible combinations of numbers for the white balls, and 26 different numbers for the red Powerball. In order to win the grand prize we need to determine one single combination of both. What is the probability that we do this? This ends un being a simple calculation since we know that there is only 1 (or $$ n $$) possible combination that ends up being the winning attempt:
{: style="text-align: justify;"}

$$ P = \frac{n}{N} =  \frac{1}{11,238,513} \times \frac{1}{26} = \frac{1}{292,201,328}$$

<div class="caption">
    A 1 in 292,201,328 chance of winning certainly feels impossible. Knowing this, you should ask yourself a single question next time you are going to buy a lottery number <p>
    <em>Do I feel lucky</em><d-footnote>Well do you, punk?</d-footnote> </p>
</div>

To calculate the probability of success for the infinite monkey theorem, we need to consider more than just the 26 letters of the English alphabet. We assume that the monkey has access to a keyboard that includes uppercase and lowercase letters, numbers, punctuation symbols, and other symbols necessary for a book (such as spaces and new lines). Altogether, this gives us about 88 inputs to work with.
{: style="text-align: justify;"}

$$ P = \frac{n}{N} =   \frac{1}{88} = 0.0113636... \approx 1.14\% $$

<div class="caption">
    The probability of each individual input
</div>

The [Gutenberg project](gutenberg.org) is repository that provides an extensive source of books that have way past expired their copyright rights. Using this resource we are able to acquire a copy of William Shakespeare's complete works in .txt format. The number of characters in "[The Complete Works of William Shakespeare](https://www.gutenberg.org/ebooks/100)" is about 5,480,868. In order for the monkey to write the full text in a single sitting becomes vanishingly small:
{: style="text-align: justify;"}

$$ P(n, N) = \frac{n}{N} = (\frac{1}{72})^{5,480,868} = 10^{-10^{7.007739000088917}}$$

This probability increases on every attempt. This implies that the event eventually happens, just that no one would be alive to confirm it:

$$ P_{\notin}(x) = (1 - P)^{x} $$

$$ P(x) = 1 - (1 - P_i)^{x} \approx 1 $$

$$P(x) = 1 - (1 - 10^{-10^{7.007739000088917}})^{x} \approx 1 $$

<div class="caption">
    Starting from the complement rule, which states that the probability of an event occurring is equal to 1 minus the probability of the event not occurring, we can find the attempt x where the event is most likely.
</div>

***

## Down to Monkey Business

The infinite monkey theorem proposes the idea that unlikely events can occur. This concept has been the subject of many simulations and studies that try to replicate this phenomenon. <d-cite key="banerji2013notion"></d-cite> However, what is more interesting is understanding the underlying mechanisms that make this possible. The theory suggests that highly ordered structures can emerge from chaos <d-cite key="gowers2008princeton"></d-cite>. While we won't attempt to simulate the entire problem, we will conduct a scenario that should produce some profound results.
{: style="text-align: justify;"}

To build our simulation, we will use computers that will act as digital counterparts to our monkeys. This way, we can accelerate the typing process by having the computer do the same work of multiple monkeys in tandem. Additionally, we need to specify the way that our 'digital monkeys' will output data. In order to get closer to theory, we also need to recreate the method in which monkeys would input characters. For this purpose, I chose the reliable [1973 IBM Selectric 721](https://typewriterdatabase.com/1973-ibm-selectric-721.19605.typewriter), as it contains all the letters and symbols that they would need.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/selectric.jpg"%}

To represent each keystroke in our simulation, we will generate a random binary number which will indicate an input. A 7-bit binary number gives us enough combinations to represent every character on the Selectric typewriter. Binary numbers have the advantage of being easy to quantify in terms of digital size. Using a typical encoding like ASCII or UTF-8, each character has a size of one byte. This means that each input to the typewriter has a size of 7 bytes (one byte per bit), and each output from the typewriter (representing a keystroke) has a size of 1 byte. To generate truly random inputs, we use the [libsodium library](https://github.com/jedisct1/libsodium) to create cryptographically secure random bytes.
{: style="text-align: justify;"}

<table style="border-collapse:collapse;border-color:#ccc;border-spacing:0;border-style:solid;border-width:1px" class="tg"><thead><tr><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal"></th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">a</th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">b</th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">c</th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">...</th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">-</th><th style="background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">=</th></tr></thead><tbody><tr><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;font-weight:bold;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">7-bit Binary</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">1100001</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">1100010</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">1100011</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">...</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">0101101</td><td style="background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;text-align:center;vertical-align:top;word-break:normal">0111101</td></tr></tbody></table>

<div class="caption">
    This is basically our translation between our binary inputs and the output from our virtual typewriter.
</div>

Now that we have our tools, let's start defining our workspace. Until the machines rise up against us, we can use any different number of 'digital monkeys' for any amount of time. Unfortunately, we still have to consider the computational cost that would allow our computer to do the work. [Google Colab](https://colab.research.google.com) is a free, cloud-based platform for running and sharing code. Although predominantly used to run Python scripts, we can use the instances provided by Colab as a computer that runs processes in the cloud. These cloud computers, like any computer, have a limit on what they can do simultaneously. Additionally, since this is a dynamic environment (resources are dependent on the number of users using the service), we cannot easily know the number of monkeys that we can assign to this task. We can definitely try to get an estimate of the optimal number of 'digital monkeys' that we can have working in parallelism. In order to do so, we can set a loop that increases the number of processes for a directly proportional set of time, and then look at the average time it takes for the process to finish.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/limit_test.jpg"%}

<div class="caption">
    This figure shows the average time it required an individual process to complete its designated task when multiple processes are executed in parallel.
</div>

At low levels of parallelism (e.g. 100 processes), the program may be able to efficiently utilize the available hardware resources without encountering bottlenecks or fight for shared resources. At high levels of parallelism (e.g. 500 processes), the program may start to encounter hardware limitations such as network bandwidth, disk I/O, or memory bandwidth that limit the overall performance of the program. Not a great look for how well optimized this simulation is, but good enough to get the data that we need. We will use 120 for our number of processes as this is the minimum value in our line of best fit.
{: style="text-align: justify;"}

In order to determine how many words we produce we need to use a dictionary. This is not your typical dictionary, as we do not require any definitions in this simulation. <d-footnote>Although the complexity of the definition could very well be an additional variable, we don't really need it right now to perceive a trend</d-footnote> This dictionary will only show us words that could be used in the english language. If money is not a problem we could use the Collins English Dictionary as a base as it includes over 722,000 words. Sadly, money <em>is</em> a problem. A free alternative that is very commonly used in these sort of problems is WordNet, which is a free lexical database that includes a respectable 155,000 words and phrases. Thankfully, [InfoChimps](http://infochimps.org) provides a sufficient dictionary with 479k English words and is freely available through a [GitHub repo](https://github.com/dwyl/english-words).

{% include figure.html path="assets/img/Monkeys/monkey_biz.png"%}

***

## All the World's a Monkey's Stage

At the end of our simulation, we managed to produce 3.7 Gbs of text in the span of 156 hours with the help of our 120 digital monkeys. So what does this look like? Let's take a look at what the data looks as a whole when we try to extract words from our whole dataset.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/initial-data.jpg"%}

<div class="caption">
    Percentage of word length in our data. Crosses represent the number of instances of the given word length divided by the total number of number of characters in our data. The curve shows the relative trend that this analysis follows.
</div>

This simply won't do. We are currently including every single character in the data, regardless if it is significant or not. Some considerations must be set to tag words in our dataset. Although the letter 'a' is a perfectly reasonable word, it leaves too much to interpretation regarding how much 'information' it provides in the text. So for this analysis, we will simply ignore any words that are made of a single character. <d-footnote>Feel free to rant on this decision down below.</d-footnote>
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/zoomed-data.jpg"%}

Our analysis shows that there is a $$15.915$$% chance that a two-letter word shows up in our dataset, and that every additional character reduces the probability exponentially. It is always wise to make sure that our results make sense. So what would be the expectation of the word length when we consider the distribution of length in our dictionary?
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/dictionary.jpg"%}

<div class="caption">
    Our dictionary contains 479k English words which include 20+ character words that are not significant during this study.
</div>

Purely from this graph, it might be logical to think that ~$$10$$ letter words should be more prevalent in our data. But to answer this inconsistency we need to go back to our probability calculations. We must remember that every consecutive character is confined by a probability. If we want a $$6$$ letter word and we currently have $$88$$ different options, then every input to our data is restricted by the distribution of this probability:
{: style="text-align: justify;"}

$$(\frac{1}{88})^{6} = \frac{1}{88} \times \frac{1}{88} \times ... \times \frac{1}{88} = \frac{1}{464,404,086,784}$$

Now that we have the probabilities in place, how does it help us determining the amount of information contained? Information theory provides us a method to quantify the amount of information contained in a file using the concept of entropy. The mere mention of entropy can cause anxiety to most scientists. It is a complex and abstract concept that is central to several fields of science. It has multiple meanings, different interpretations, and a wide array of formulations. More than anything, people find it non-intuitive. In this case, entropy measures the amount of uncertainty or randomness in a system. In information theory, it represents the amount of uncertainty or randomness in data.
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/entropy.jpg"%}

A file contains more information if its data is more unpredictable, according to the basic principle behind quantifying information using entropy. Entropy is calculated by identifying all possible outcomes or symbols that can appear in a file. These symbols can be anything from individual characters in a text file to individual bits in a binary file. The entropy of information can be calculated using the following formula:
{: style="text-align: justify;"}

$$H(p_i) = -Σ \enspace p_i \enspace log_2 \space p_i$$

Where $$H$$ is the entropy of information, $$p_i$$ is the probability of symbol $$i$$ occurring, and $$log_2$$ is the base-2 logarithm.
{: style="text-align: justify;"}

Let's consider the entropy of information for "The Complete Works of William Shakespeare" first. After filtering out all the copyright and index contents, we are left with 959,976 words. 
{: style="text-align: justify;"}

{% include figure.html path="assets/img/Monkeys/shakespeare_data.jpg"%}

<div class="caption">
    Probability of word length in "The Complete Works of William Shakespeare"
</div>

Calculating the entropy requires us to define a probability distribution that a word of a particular length would be found in the file:
{: style="text-align: justify;"}

$$ p_i = \frac{\text{Number of instances}}{\text{Total number of words}}$$

$$ \qquad $$

$$ H(p_i) = -Σ \enspace p_i \enspace log_2 \space p_i = 2.839 \text{bits}$$

Performing the same calculation to our simulation data we get that the entropy of information based on word length is $$1.242$$ bits, which is quite strange. Why would we get a lower entropy when the creation of this data has been completely random? The entropy we got from our simulation is not a mistake. Claude Shannon calculated the conditional entropy of English text based on letter frequencies, but the method can be adapted to word frequencies as well. Shannon found that the entropy per letter of English text was about $$1.3$$ bits. <d-cite key="shannon1951prediction"></d-cite> Both this simulation and Shannon's work assumes that the letters or words in the text are independent and identically distributed. However, in natural language, there are often patterns and correlations between words, which can increase the conditional entropy. Additionally, the frequency of longer words that is found in the works of Shakespeare leads to a higher uncertainty.
{: style="text-align: justify;"}

Let's do one final calculation. We did not consider the effect that cases would have on the readability of the file. Meaning that so far, 'Hello World' and 'helLo wORlD' are the same. To rectify this, let's consider 'penalizing' the word count for every mistake in the word. Meaning that 'enTRopy' would be counted as a $$5$$ letter word instead of $$7$$. For example, the probability of finding a two letter word is now $$12.227$$% instead of the previous $$15.915$$%. By doing this, we've increased the entropy of information based on word length to $$1.328$$ bits. Which inches us closer to the entropy found in Shakespeare's work.
{: style="text-align: justify;"}

## Where art thou my Entropy?

You might be wondering the difference between these 'bits' from entropy and the 'bits' encoded in the vast sum of XX Gbs in our data. <d-footnote>1 GB = 1,073,741,824 bytes * 8 bits/byte = 8,589,934,592 bits</d-footnote> The bits in a file size refer to the amount of storage required to represent the contents of a file, while the bits in the entropy of information refer to the amount of uncertainty or randomness in a given set of information. That being said they both refer to the same unit value. One could infer from the large difference of these values, that the contents contain a large amount of redundancy.
{: style="text-align: justify;"}

> *Tomorrow and tomorrow and tomorrow <br />Creeps in this petty pace from day to day <br />To the last syllable of recorded time, <br />And all our yesterdays have lighted fools <br />The way to dusty death. Out, out, brief candle! <br />Life's but a walking shadow, a poor player <br />That struts and frets his hour upon the stage <br />And then is heard no more. It is a tale <br />Told by an idiot, full of sound and fury, <br />Signifying nothing* <d-footnote>In many theatre groups, the implication of redundancy might earn you a beating.</d-footnote>

By this measure, a highly compressed cat video contains an entropy much larger than its file size. This video would have very little redundancy in its data. But the significance of the information in the The Bard's work is inherently more valuable. <d-footnote>Again, feel free to rant in regards to this statement down below.</d-footnote> This doesn't change our definition of information, but instead sheds some light on what we mean by entropy.
{: style="text-align: justify;"}

Originally, the word "entropy" was coined by German physicist Rudolf Clausius in 1865. It is derived from the Greek words "en," meaning "in," and "tropos," meaning "turn" or "transformation." Clausius used the term to describe a measure of the amount of energy in a system that is no longer available to do useful work. Although this definition is still used, and is perfectly reasonable in large systems, when physicists refer to the entropy of a system they talk about a measurement of how much of the system we are not sure of. 