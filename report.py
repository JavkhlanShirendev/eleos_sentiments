import static


class Sentiments(object):
  # sentiments = []
  sentiments_sorted = {}

  def append(self, sentiment_item):
    # self.sentiments.append(sentiment_item)
    ticker_symbol = sentiment_item.ticker_symbol
    self.sentiments_sorted[ticker_symbol] = self.sentiments_sorted.get(ticker_symbol, {'median': 0, 'median_max': 0, 'list': []})
    if len(self.sentiments_sorted[ticker_symbol]['list']) == 0:
      self.sentiments_sorted[ticker_symbol]['list'].append(sentiment_item)
      self.sentiments_sorted[ticker_symbol]['median_max'] +=  sentiment_item.subjectivity * sentiment_item.polarity 
      self.sentiments_sorted[ticker_symbol]['median'] =  sentiment_item.subjectivity * sentiment_item.polarity
      if static.debug_mode:
        print ("s: %f:, p: %f, l: %d" % (sentiment_item.subjectivity, sentiment_item.polarity, 1))
        print ("median_max: ", self.sentiments_sorted[ticker_symbol]['median_max'])
        print ("median: ", self.sentiments_sorted[ticker_symbol]['median']) 
      return

    added = False
    for i in range(len(self.sentiments_sorted[ticker_symbol]['list'])):
      old_sort_index = self.sentiments_sorted[ticker_symbol]['list'][i].subjectivity * self.sentiments_sorted[ticker_symbol]['list'][i].polarity
      sort_index = sentiment_item.subjectivity * sentiment_item.polarity
      if old_sort_index > sort_index:
        added = True
        self.sentiments_sorted[ticker_symbol]['list'].insert(i, sentiment_item)
        break

    if not added:
      self.sentiments_sorted[ticker_symbol]['list'].append(sentiment_item)

    self.sentiments_sorted[ticker_symbol]['median_max'] = self.sentiments_sorted[ticker_symbol]['median_max'] + sentiment_item.subjectivity * sentiment_item.polarity
    self.sentiments_sorted[ticker_symbol]['median'] = self.sentiments_sorted[ticker_symbol]['median_max'] / len(self.sentiments_sorted[ticker_symbol]['list'])

    if static.debug_mode:
      print ("s: %f:, p: %f, l: %d" % (sentiment_item.subjectivity, sentiment_item.polarity, len(self.sentiments_sorted[ticker_symbol]['list'])))
      print ("median_max: ", self.sentiments_sorted[ticker_symbol]['median_max'])
      print ("median: ", self.sentiments_sorted[ticker_symbol]['median'])

  def report(self):
    for key, items in self.sentiments_sorted.items():
      print ("key: %s, median: %f" % (key, items['median']))
      # print ("items: ", items)
      for i in range(len(items['list'])):
        print ("%d: %s" % (i, items['list'][i]))

      print ()
      print ()