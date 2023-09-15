<!-- ABOUT THE PROJECT -->

## About The Project

Our project aims to learn and apply machine learning techniques to predict stock prices and trends in the stock market.
We will be building a web application that will predict U.S. stock market prices. We will focus on the US stock market
and the large companies that are part of the Standards and Poor (S&P) 500, a stock market index that tracks the
performance of these large companies. Some of these are Apple, Google, Amazon, and Microsoft.

We divided our project into several strategies. In each one, we used different machine learning techniques that we have
learned in this course to improve and get the best-predicted trading results that simulate the actual trending. Some of
the strategies that will be used to predict the direction of the stock trend will be based on the dataset, and others
can indicate a stock price for a specific day. Moreover, we will compare the results between the strategies to see which
one was more accurate.

| Type                | Sub Type       | Algorithm                             |
|---------------------|----------------|---------------------------------------|
| Supervised Learning | RNN              | [LTSM](ltsm_stock_market_prediction/) |

### Built With

This section lists all major frameworks/libraries used to bootstrap this project.

* [![Python][Python.org]][Python-url]
* [![Jupyter][Jupyter.org]][Jupyter-url]
* [![Miniconda][Miniconda.com]][Miniconda-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Following the instructions below should get you up and running and quickly as possible without googling around to run
the code.

### Prerequisites

Below is the list things you need to use the software and how to install them. Note, these instructions assume you are
using a Mac OS. If you are using Windows you will need to go through these instructions yourself and update this READ
for future users.

1. pyenv
   ```sh
    brew update
    brew install pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
2. python
   ```sh
    pyenv install 3.9.5   
    pyenv global 3.9.5 
   ```

3. poetry
   ```sh
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
   ```

4. miniconda
   ```sh
   cd /tmp
   curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
   bash Mambaforge-$(uname)-$(uname -m).sh
   ```

5. Restart new terminal session in order to initiate mini conda environmental setup

6. Git LFS
   ```sh
   brew install git-lfs
   ```

### Installation

Below is the list of steps for installing and setting up the app. These instructions do not rely on any external
dependencies or services outside of the prerequisites above.

1. Clone the repo
   ```sh
   git clone git@github.com:fall2023csce5214/ltsm_stock_market_prediction.git
   ```
2. Install project
   ```sh
   poetry install
   poetry run pip install tensorflow==2.13.0
   conda env create -f environment.yml
   conda activate ltsm_stock_market_prediction
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

In order to view or execute the various notebooks run the following command on any of the sub folders in this directory.

Here is an example to launch the LTSM Notebook.

```sh
jupyter notebook
```

Once inside the
notebook [use the following link](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html)
on examples of how to use the notebook.

Here is an example to launch pytest to run the unit test on the command line.  Note, you can also use your favorite IDE if you point it to the python interpreter that your poetry virtual environment is running from.

```sh
poetry run python -m pytest -k test_appl_ltsm_60_day_model
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DESIGN -->

## TBD

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the GNU License. See `LICENSE.md` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Jibril Moalim - Jibrilmoalim@gmail.com
<p/>
Lakshmi Prasanna Valdas - lakshmiprasannavaldas@my.unt.edu
<p/>
Larry Johnson - johnson.larry.l@gmail.com
<p/>
Monish Galla - monishgalla@my.unt.edu
<p/>
Vamshidhar Reddy Venumula - vamshidharreddyvenumula@my.unt.edu
<p/>

Project Link: [https://github.com/fall2023csce5214/ltsm_stock_market_prediction/](https://github.com/fall2023csce5214/ltsm_stock_market_prediction/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Jupyter-url]:https://jupyter.org

[Jupyter.org]:https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white

[Python-url]:https://python.org

[Python.org]:https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Miniconda-url]:https://docs.conda.io/

[Miniconda.com]:https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white