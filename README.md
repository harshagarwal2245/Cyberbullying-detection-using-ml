[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs) 

![Stars](https://img.shields.io/github/stars/harshagarwal2245/Cyberbullying-detection-using-ml)

![Issues](https://img.shields.io/github/issues/harshagarwal2245/Cyberbullying-detection-using-ml) 

![Build](https://img.shields.io/github/workflow/status/harshagarwal2245/Cyberbullying-detection-using-ml/Cyberbullying%20Detection) 

![Build Event Status](https://img.shields.io/github/workflow/status/harshagarwal2245/Cyberbullying-detection-using-ml/Cyberbullying%20Detection)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d31c7ae536849259d5365c4935a88ac)](https://www.codacy.com/gh/harshagarwal2245/Cyberbullying-detection-using-ml/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=harshagarwal2245/Cyberbullying-detection-using-ml&amp;utm_campaign=Badge_Grade)

![Deployment](https://img.shields.io/github/deployments/harshagarwal2245/Cyberbullying-detection-using-ml/cyberbullying-detection12) 

# Detecting Cyberbullying on social media using Machine Learning

With the exponential increase of social media users, cyber bullying 
has been emerged as a form of bullying through electronic messages. 
Social networks provide a rich environment for bullies to uses 
these networks as vulnerable to attacks against victims. Given the 
consequences of cyber bullying on victims, it is necessary to find 
suitable actions to detect and prevent it. Recently, deep neural 
network-based models have shown significant improvement over 
traditional models in detecting cyberbullying. Also, new and more 
complex deep learning architectures are being developed which are 
proving to be useful in various NLP tasks. The model is trained 
and evaluated on dataset that is provided by Dataturks. The dataset 
contained 20000 tweets gathered manually annotated by human experts. 
Selected Twitter-based features namely text and network-based features 
were used. Several classifiers are trained for determining cyberbullying.

## Features

- Manual, script-driven, and interactive process 
- Deployment is in form of prediction service which contains both API and webapp
- Code had been modularized in form of pipelines for experimentation purpose
- Cross Platform

## Tech Stack

**Client:** Css, Html

**Server:** Flask, Python, Sklearn


## Screenshots

![App Screenshot](https://github.com/harshagarwal2245/Cyberbullying-detection-using-ml/blob/main/visvualization/interface.png)


## Demo

The video shows two different comments and it prediction using software. and how can user use it


https://user-images.githubusercontent.com/55704229/166684735-c1eab1ff-a6a0-472c-bc96-1f5bd6584cf0.mp4




## Installation

- Install Python version 3.8
- Install git
- On bash
 ``` git clone https://github.com/harshagarwal2245/Cyberbullying-detection-using-ml.git ```
- Create virtual envoirment
``` conda create -n cyberbullying3 python=3.8 -y ``` 
- Install the requirements using pip command
``` pip install -r requirements.txt ```
- Run app using python app.py
## API Reference



#### Get Prediction

```http
  GET https://cyberbullying-detection12.herokuapp.com/api/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`      | `string` | **Required**. comment for Prediction |

Takes comment and predict weather given comment contains cyberbullying
activities or not


## Usage/Examples

```python
import requests
import json

url = "http://127.0.0.1:5000"

payload = json.dumps({
  "text": " best memory with your friends (place  when  what you did)"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```


## Running Tests

To run tests, run the following command

```bash
  tox -r
```


## Support

For support, email agarwalharsh244@gmail.com.


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are always welcome!
Please adhere to this project's `code of conduct`.


## Acknowledgements

 I would like to take this opportunity to thank my internal guide 
 Prof. Shrikant Dhamdhere for giving us all the help and guidance 
 I needed. I am really grateful to them for their kind support. 
Their valuable suggestions were very helpful. I am also grateful to Prof. Shrikant Dhamdhere, Head of Computer Engineering Department, 
Parvatibai Genba Moze College of Engineering, Wagholi Pune-412207 
for his indispensable support, suggestions. In the end our special 
thanks to Prof.Pramod Dhamdhere for providing various resources such as 
laboratory with all needed software platforms, continuous Internet
connection, for Our Project.

## Feedback

If you have any feedback, please reach out to us at agarwalharsh244@gmail.com


## Authors

- [@Harsh Agarwal](https://www.github.com/harshagarwal2245)
- [@Jagruti Jadhav](https://www.github.com/jagrutijadhav)
- [@Komal Nagar](https://www.github.com/komalnagar)

