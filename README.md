# Baby Got Backend - Language Analyzer
### Introduction

### Installation

### How to Use BGB

### Module Functionality

The main language analyzer module is composed of three discrete analysis modules: one for sentiment analysis, one for domain analysis, and one for behavior analysis. When the user enters a phrase, an instance of the top-level language analyzer module is created, and on that module, a new instance of each analysis module is also created. Each of those modules receives its own tokenizer, which does some basic phrase processing when instantiated and opens up methods for further processing as needed within each module.

##### Report Calculation

When the language analyzer calculates a report from a phrase, it first breaks the phrase down into a list of sentences. The words in each sentence are then weighted based on their relationship to the other words in the sentence, rather than the words in the overall phrase. After each sentence is considered on its own, a full phrase report is calculated by combining the reports of individual sentences.

##### ...
