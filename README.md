# Al Yamamah Ai

An AI service designed for Al Yamamah University to enhance productivity, streamline academic and administrative tasks, and provide cutting-edge solutions powered by OpenAI's API.


## Description

Al Yamamah AI is a platform tailored to serve the academic and administrative needs of Al Yamamah University. It integrates the capabilities of OpenAI's API to offer intelligent solutions, such as content generation, automated grading assistance, and student advisory support. This project aims to bridge the gap between advanced AI and everyday university processes, making them more efficient and accessible.


## Getting Started

### Dependencies

* Python 3.9 or higher
* Django 4.2+
* OpenAI Python SDK and API key
* django-tailwind

### Installing

#### 1-Clone the repository from GitHub:
```
git clone https://github.com/your-repo/Al-Yamamah-AI.git
cd Al-Yamamah-AI
```
#### 2-Install required Python libraries:
```
pip install -r requirements.txt
```
#### 3-Configure the .env file with your OpenAI API key
```
SECRET_KEY = "SECRET_KEY"
API_KEY = "API_KEY"

```


### Executing program

* How to run the program
* Step-by-step bullets
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
open anther terminal to run the tailwind dependence
```
python manage.py tailwind start
```

## Help

common issues:

* Ensure Python and Django are installed correctly.
* Verify your API key is active and correctly placed in the .env file.
* Use the following command to troubleshoot:
`python manage.py check`

## Author

Fayez Al-Qhatani<br>

* X: [@Fayez Alshwayya](https://x.com/Fayez_Alshwayya)
* Website: [@Fayez Alshwayya](https://fayezs.site)

## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
