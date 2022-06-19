""""The (X)Path to CSS Locators
Many people prefer using CSS Locator notation to XPath notation. As we will see later, it often makes attribute selection very easy. To help get you more comfortable going back and forth between XPath and CSS Locator strings, we give you a chance in this exercise to do some direct "translation" between the two.

Note that the exercises in this chapter may take some time to load.""""


# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = "html>body>span:nth-of-type(1) a"


# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'