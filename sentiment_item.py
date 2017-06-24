class SentimentItem(object):
  print_format = "%s -- m: %d, p: %s, s: %s\n %s"

  def __init__(self, text, ticker_symbol, **kwargs):
    self.text = text
    self.ticker_symbol = ticker_symbol
    self.multiplier = kwargs.get('multiplier', 0) + 1
    self.polarity = kwargs['polarity']
    self.subjectivity = kwargs['subjectivity']

  def __str__(self):
    return (self.print_format % ("#" + self.ticker_symbol, self.multiplier, self.polarity, self.subjectivity, self.text))

  def __unicode__(self):
    return (self.print_format % ("#" + self.ticker_symbol, self.multiplier, self.polarity, self.subjectivity, self.text))