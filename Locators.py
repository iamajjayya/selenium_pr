'''

Locators

-> Locators are addresses that identify web elements uniquely within th e page

->, Locators
    1, ID
    2, name
    3, Class Name
    4, linkText
    5, Partial Link Text
    6, TagName
->, Customized Locators
    7, CSS Selector

    8, XPATH ->  xpath is an address of the element
       -> Absolute xpath / full xpath  /html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a
       -> Relative xpath / Relative or partial path //*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a


       diff between Absolute and relative xpath

       1, Axpath start from root html node
          Rxpath xpath directly jump to element on dom

       2, Axpath xpath start with /
          Rxpath xpath start with //

       3, Axpath xpath we use only tags/nodes
          Rxpath we use attributes


          Syntax of writing relative xpath

          //tagname[@attribute='value']


          xpath options
          -------------
           and
           or
           contains()
           start-with()
           text()

         Xpath axes

         ->  Self
         -> parent
         -> child
         -> ancestor
         -> descendant
         -> following
         -> following -sibling
         -> preceding
         -> preceding -  sibling




'''