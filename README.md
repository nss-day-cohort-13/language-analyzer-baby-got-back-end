# Baby Got Backend - Language Analyzer
### Introduction

### Installation

### How to Use BGB

### How it works

The main language analyzer module is composed of three discrete analysis modules: one for **sentiment analysis**, one for **domain analysis**, and one for **behavior analysis**. When the user enters a phrase, an instance of the top-level language analyzer module is created, and on that module, a new instance of each analysis module is also created. Each of those modules receives its own tokenizer, which does some basic phrase processing when instantiated and opens up methods for further processing as needed within each module.

#### Report Calculation

When the language analyzer calculates a report from a phrase, it first breaks the phrase down into a list of sentences. The words in each sentence are then weighted based on their relationship to the other words in the sentence, rather than the words in the overall phrase. After each sentence is considered on its own, a full phrase report is calculated by combining the reports of individual sentences.

#### Module Functionality

For the most part, each analysis module operates indepedently of the others. When instantiated, the analysis modules receive the phrase the user entered from the top-level language analyzer module, and they use the tokenizer to process the phrase. Each module has a corresponding section in our lexicon file that allows the modules to identify keywords in the phrase to use when calculating a report.*

The only exception to the rule that each module operates independently is the sentiment analysis module. This module depends on values that result from behavior analysis to create its final report, so the sentiment analysis module has its own instance of a behavior analysis module for retrieving the needed values.

When final calculations are complete for each module, the individual modules print their own report of the analysis in the terminal, giving each sentiment, behavior, or domain represented in the phrase a value between 0 and 1, with total values adding up to 1 (or 100%). Currently, our program is only set up to completely analyze three phrases that we categorized in our lexicon for the MVP build. Future versions of the program will include a more robust lexicon that will allow for the analysis of more words and phrases.

**For our lexicon of positive and negative words, we thank the [MPQA](http://mpqa.cs.pitt.edu/lexicons/effect_lexicon/) at the University of Pittsburgh, specifically Yoochung Choi and Janyce Wiebe for their work on the +/- Effect Lexicon project, and [Neal Caren](http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-3/) for his additional breakdown of the Choi and Wiebe's work.*
