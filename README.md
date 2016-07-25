# Baby Got Backend - Language Analyzer
### Introduction

### Installation

### How to Use BGB

### Module Functionality

The main language analyzer module is composed of three discrete analysis modules: one for sentiment analysis, one for domain analysis, and one for behavior analysis. When the user enters a phrase, an instance of the top-level language analyzer module is created, and on that module, a new instance of each analysis module is also created. Each of those modules receives its own tokenizer, which does some basic phrase processing when instantiated and opens up methods for further processing as needed within each module.

##### Sentiment Analysis
