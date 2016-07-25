# Language Analyzer Group Project

## NSS Team Project

### Introduction
#### Team Members: (See us on GitHub)
 - [Chase Ramsey]
 - [Tekisha Hammock]
 - [Cory Tohill]
 - [Simon Herrera]

### Information

The team was instructed to build a language analyzer while meeting 2 requirements...

- A full test suite: There should be no logic for which there is not a test.
- Documentation: Every class and every method should have a docstring.

The Language Analyzer itself should analyze test statements and output a report of its analysis of Sentiment, Behavior and Domain in a numerical range between 0 and 1.

### Basic functionality of each Module:
**Tokenizer** contains methods that are called as needed to parse the original message.

**Behavior Predictor** determines what behaviors are present in the message, prints a report and pass those behaviors in a list to the Sentiemetn Module.

**Sentiment Analysis** shows what percentage positive, negative or neutral the statement is. The inherited behaviors have a slight factor on the overall sentiment.

**Domain Identifier** determines the subject matter of the message.

   [chase ramsey]: <https://github.com/chase-ramsey>
   [tekisha hammock]: <https://github.com/tekishahammock>
   [cory tohill]: <https://github.com/CoryTohill>
   [simon herrera]: <https://github.com/SimonHerrera>



### Installation
* BGB requires [Python](https://www.python.org/downloads/) v3.3.6+ to run.
* Fork or clone the GitHub repository into a project folder.

### How to Use BGB
* In the terminal, navigate to the project folder
* To execute the program, run the following command in the terminal:
    ```
    python lang_py.py
    ```
* A command prompt should appear asking for a phrase to analyze. Type in the phrase you want analyzed and press enter to run the analysis.
* The analysis includes:
    * __Sentiment Analysis__ - Percentage of how overall positive, negative, neutral a phrase is.
    * __Behavior Analysis__ - Percentage of behaviors present, e.g. Aggressive, Social.
    * __Domain Analysis__ - Percentage of domains/topics the phrase is about, e.g. Transportation
* Phrases that work with v1.0 of BGB:
    * The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal.
    * How would your life be different if you stopped making negative judgmental assumptions about people you encounter? Let today be the day you look for the good in everyone you meet and respect their journey.

### How it works

The main language analyzer module is composed of three discrete analysis modules: one for **sentiment analysis**, one for **domain analysis**, and one for **behavior analysis**. When the user enters a phrase, an instance of the top-level language analyzer module is created, and on that module, a new instance of each analysis module is also created. Each of those modules receives its own tokenizer, which does some basic phrase processing when instantiated and opens up methods for further processing as needed within each module.

#### Report Calculation

When the language analyzer calculates a report from a phrase, it first breaks the phrase down into a list of sentences. The words in each sentence are then weighted based on their relationship to the other words in the sentence, rather than the words in the overall phrase. After each sentence is considered on its own, a full phrase report is calculated by combining the reports of individual sentences.

#### Module Functionality

For the most part, each analysis module operates indepedently of the others. When instantiated, the analysis modules receive the phrase the user entered from the top-level language analyzer module, and they use the tokenizer to process the phrase. Each module has a corresponding section in our lexicon file that allows the modules to identify keywords in the phrase to use when calculating a report.*

The only exception to the rule that each module operates independently is the sentiment analysis module. This module depends on values that result from behavior analysis to create its final report, so the sentiment analysis module has its own instance of a behavior analysis module for retrieving the needed values.

When final calculations are complete for each module, the individual modules print their own report of the analysis in the terminal, giving each sentiment, behavior, or domain represented in the phrase a value between 0 and 1, with total values adding up to 1 (or 100%). Currently, our program is only set up to completely analyze three phrases that we categorized in our lexicon for the MVP build. Future versions of the program will include a more robust lexicon that will allow for the analysis of more words and phrases.

**For our lexicon of positive and negative words, we thank the [MPQA](http://mpqa.cs.pitt.edu/lexicons/effect_lexicon/) at the University of Pittsburgh, specifically Yoochung Choi and Janyce Wiebe for their work on the +/- Effect Lexicon project, and [Neal Caren](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-3/) for his additional breakdown of the Choi and Wiebe's work.*
