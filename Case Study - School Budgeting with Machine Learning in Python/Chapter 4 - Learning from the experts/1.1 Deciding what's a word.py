'''
Deciding what's a word
Before you build up to the winning pipeline, it will be useful to look a little deeper into how the text features will be processed.

In this exercise, you will use CountVectorizer on the training data X_train (preloaded into the workspace) to see the effect of tokenization on punctuation.

Remember, since CountVectorizer expects a vector, you'll need to use the preloaded function, combine_text_columns before fitting to the training data.

Instructions
100 XP
Instructions
100 XP
Create text_vector by preprocessing X_train using combine_text_columns. This is important, or else you won't get any tokens!
Instantiate CountVectorizer as text_features. Specify the keyword argument token_pattern=TOKENS_ALPHANUMERIC.
Fit text_features to the text_vector.
Hit 'Submit Answer' to print the first 10 tokens.
'''

# Import the CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create the text vector
text_vector = combine_text_columns(X_train)

# Create the token pattern: TOKENS_ALPHANUMERIC
TOKENS_ALPHANUMERIC = '[A-Za-z0-9]+(?=\\s+)'

# Instantiate the CountVectorizer: text_features
text_features = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC)

# Fit text_features to the text vector
text_features.fit(text_vector)

# Print the first 10 tokens
print(text_features.get_feature_names()[:10])