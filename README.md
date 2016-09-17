
#Corner Case Logics
1.If one operator is following another operator, I just simly ignore the second operator. If a use types a series of operators, the calculator will only consider the first operator.



2.If a number will be divided by zero, I will return "ERROR" when next click happens.



#GET vs POST
I chose GET method for my calculator.
First, I don't store any data and the backend code only does calculation. Besides, the data in the request are current input digit and previous result and operator. It's okay if users see the information in browser. As it's not necessary to worry about data safety, even GET is less secure than POST, I prefer to use GET which is more convenient and easier.


Second, the restriction on data type for GET method will not influence the calculator since users only pass in numbers and operators in string type.


Third, as I use GET to generate requests and the parameters will be passed in URL, other application/program can mock requests to my calculator and use its function. It's like an API and is more friendly to developers.


