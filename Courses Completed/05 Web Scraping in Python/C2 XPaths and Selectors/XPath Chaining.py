"""XPath Chaining
Selector and SelectorList objects allow for chaining when using the xpath method. What this means is that you can apply the xpath method over once you've already applied it. For example, if sel is the name of our Selector, then

sel.xpath('/html/body/div[2]')
is the same as

sel.xpath('/html').xpath('./body/div[2]')
or is the same as

sel.xpath('/html').xpath('./body').xpath('./div[2]')
The only catch is that you need to "glue together" the XPath pieces by using a period at the start of each subsequent XPath string (notice the periods we added to the XPath strings in our examples).

Instructions
100 XP
Instructions
100 XP
Fill in the blank below to chain together two xpath calls which result in the same selection as
sel.xpath('//div/span/p[3]')"""

# Chain together xpath methods to select desired p element
sel.xpath( '//div' ).xpath( './span/p[3]')