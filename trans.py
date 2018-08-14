#!coding:utf-8
from googletrans import Translator
translator = Translator()
content = '''
&lt;p&gt;I am following &lt;a href=&quot;https://stevenmiller888.github.io/mind-how-to-build-a-neural-network/&quot; rel=&quot;nofollow noreferrer&quot;&gt;this&lt;/a&gt; article to build 'hello world' in the world of neural networks - XOR.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;During the back-propagation phase author calculates changes in weights between input and hidden layer by calculating &lt;/p&gt;&#xA;&#xA;&lt;p&gt;&lt;a href=&quot;https://i.stack.imgur.com/7BkIL.png&quot; rel=&quot;nofollow noreferrer&quot;&gt;&lt;img src=&quot;https://i.stack.imgur.com/7BkIL.png&quot; alt=&quot;enter image description here&quot;&gt;&lt;/a&gt;&lt;/p&gt;&#xA;&#xA;&lt;p&gt;where&lt;/p&gt;&#xA;&#xA;&lt;pre&gt;&lt;code&gt;w - weights between input and hidden layer&#xA;Hsum - change in the hidden layer sum&#xA;I - input value to  node in NN&#xA;&lt;/code&gt;&lt;/pre&gt;&#xA;&#xA;&lt;p&gt;While this works for input values of 1, it naturally won't work for input values 0. Is it author's mistake and I should look for a better source of learning or I am missing something here?&lt;/p&gt;&#xA;
''' 

translation = translator.translate(content, dest='zh-cn')
print(translation.text)
