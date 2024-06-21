import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib

st.title('How to avoid DeReLiCT Code')

st.write("Basic steps to help avoid total code collapse.")

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Why?","**De**", "**Re**", "**Li**", "**C**", "**T**"])

with tab0:
    st.write("If you have written a piece of code that has contributed to the development of results that you plan on publishing as a research article,",
             "that code needs to be available for peer review and scrutiny in the same way your methods and results are.",
             "These steps help you to ensure that you've done your due diligence in providing your workings.")
    st.write("If you've worked hard to produce a piece of scientific software that solves a specific research problem,",
             "you want to make sure that other people can actually use your code! You don't want it to languish simply because",
             "you have forgotten to include a license file or some other detail.")
    st.write("You don't want to face calamity when one of the libraries you have used updates and suddenly there are version conflicts",
             "and nothing works anymore. You ideally want to be able to return in the fututre and reproduce the results you initially",
             "generated months ago.")
    st.subheader("These are the easy, bare-minimum steps you should take to ensure your scientific code and subsequent results are robust and reproducible.")

with tab1:
    st.header("Dependencies: record them!")
    
    st.write("You might hear researchers or code users complain about [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell).",
             "While juggling dependencies occurs at every level of computing, we are going to focus specifically on your scientific code,",
             "and how to avoid future errors and issues with reproducibility by recording your dependencies.")
    st.write("Regardless of the language you are using to write your scientific research code, there will be different versions of the language itself,",
             "and different versions of the plug-ins and libraries you use.",
             "If you fail to record what version of which libraries you use, you may run into compatibility errors when certain libraries are updated.",
             "Even worse, the behaviour of a library may change and your code can produce *different* results, without any obvious errors.")
    st.write("[NYU Libraries](https://guides.nyu.edu/software-reproducibility/dependencies) provides some straightforward guidance to help you begin, summarised in brief below.")
    st.subheader("1. Use dependencies wisely and sparingly")
    st.write("Don't import dependencies you don't actually use, and try to stick to libraries that have robust and stable releases.")
    st.subheader("2. Use a package manager of some form")
    st.write("A multitude of different package managers exist to help you isolate specific dependencies in a virtual environment for a specific project.",
             "Some popular package managers for Python and R include Conda and renv. Read more about Python package management tools [here](https://alpopkes.com/posts/python/packaging_tools/),",
             "and about R dependency management [here](https://ecorepsci.github.io/reproducible-science/renv.html).")
    st.subheader("3. Record your dependencies in a metadata file")
    st.write("Depending on the package management software and coding language you are using, there are a range of different metadata formats available",
             "to you to record your package versions.",
             "Package managers allow you to export a file with the specific versions of all used libraries/modules/packages, which can then be used",
             "to recreate the same environment elsewhere and reproduce the code results.",
             "Some of the most popular metadata filetypes for Python dependency management are shown below in the bar plot, using data",
             "from JetBrains Python Developers Survey (2022).")
    # https://lp.jetbrains.com/python-developers-survey-2022/
    # Copyright © JetBrains s.r.o. 2023
    # cc-by-4.0
    where_dependencies = {
        
        "requirements.txt" : 69,
        "pyproject.toml": 33,
        "poetry.lock": 25,
        "pipfile.lock": 15,
        "Conda environment.yml": 11,
        "pip constraints.txt": 6,
        "Other": 4,
        "None": 4,
    }

    tools_for_dependencies = {
        "poetry": 30,
        "pipenv": 28,
        "pip-tools": 26,
        "Other" : 4,
        "None": 28,
    }


    df_where_dep = pd.DataFrame.from_dict(where_dependencies, orient='index', columns=["Percentage"]).sort_values("Percentage").reset_index()
    df_tools = pd.DataFrame.from_dict(tools_for_dependencies, orient='index', columns=["Percentage"]).sort_values("Percentage").reset_index()

    st.altair_chart(
        alt.Chart(df_where_dep).mark_bar(
            size=40,
            cornerRadiusBottomRight=3,
            cornerRadiusTopRight=3
            ).encode(
        y=alt.Y('index').sort('-x'),
        x='Percentage',
        color=alt.Color("Percentage", legend=None).scale(scheme="bluepurple")).properties(
            height=alt.Step(50),
            title="What format is your application dependency information stored in?").configure_axis(
        labelFontSize=20,
        titleFontSize=20
    ).configure_axisY(labelAlign="right", labelLimit=300, title=None).configure_title(
        fontSize=20, color="gray"),
        use_container_width=True,
        
    )
    st.write("Responders could select more than one option. The total may be greater than 100% for this multiple-answer question.",
             "*Data from Python developers survey 2022. Copyright © JetBrains s.r.o. 2023.*")
    
    st.header("Going further")
    st.write("Another way to avoid dependency issues and ensure reproducible coding environments is to implement containerisation.",
             "You can create a lightweight **container** which includes a specific operating system and",
             "only the code and libraries required to run your code. Read this ['What is containerisation?'](https://www.ibm.com/topics/containerization) article,",
             "or this ['Introduction to Containers and Docker'](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/) documentation.")
    st.write("Many different container technologies, platforms and softwares exist, including [Docker](https://www.docker.com/),",
             "[Singularity](https://docs.sylabs.io),",
             "and [Apptainer](https://apptainer.org/).")
    st.write("Containerisation can support and accelerate research computing on HPC systems,",
             "and is straightforward to set up within a workflow that already uses a package manager of some form, such as conda.")

    # st.subheader('Which tools do you use for application dependency management?')
    # st.write("Responders could select more than one option. The total may be greater than 100% for this multiple-answer question.")
    # st.write("*Data from Python developers survey 2022. Copyright © JetBrains s.r.o. 2023.*")
    # st.altair_chart(
    #     alt.Chart(df_tools).mark_bar(
    #         size=40,
    #         cornerRadiusBottomRight=3,
    #         cornerRadiusTopRight=3
    #         ).encode(
    #     y=alt.Y('index').sort('-x'),
    #     x='Percentage',
    #     color=alt.Color("Percentage", legend=None).scale(scheme="bluepurple")).properties(height=alt.Step(50)).configure_axis(
    #     labelFontSize=20,
    #     titleFontSize=20
    # ).configure_axisY(labelAlign="right", labelLimit=300, title=None),
    #     use_container_width=True,
        
    # )

with tab2:
    st.header("Repository: use one!")
    st.write("A repository with version control is a folder that contains all of your code and its associated documentation",
             "(including the metadata with all your dependencies as discussed in the previous step!),",
             "that is publicly shared and has some form of change tracking that allows you to roll back to previous versions of the code.")
    st.write("The [FAIR software](https://fair-software.nl/recommendations/repository) website, built by the Netherlands eScience Center and DANS,",
             "suggests that you should **'use a publicly accessible repository with version control'**.")
    st.write("This ensures:")
    st.subheader("1. Your code can be scrutinized")
    st.write("A publicly available repository allows your peers to download your code, read it, and test it.",
             "True peer review of any paper containing results generated with code is not possible without the code also being available.",
             "Using a public repository makes it easier to share this code during the review process without relying on emailing different versions",
             "of code scripts back and forth.")
    st.subheader("2. Your code can be used and improved upon")
    st.write("A publicly available repository allows you to easily collaborate with other researchers.",
             "It provides an easy method of access to and installation of the code."
             "Various version control systems have robust tools to handle multiple code authors collaborating in real time.")
    st.subheader("3. Your can rewind mistakes indefinitely")
    st.write("The key benefit of specifically using a version-controlled repository is that you can easily roll back to previous versions",
             "of your code if you accidentally introduce a breaking change.",
             "Additionally, each version of your code is retrievable, meaning it can be assigned a unique identifier such as a DOI, so that",
             "you can cite the specific version of your code you used in a project.")
    st.header("What version control system should I use?")
    st.write("Again, the [FAIR software](https://fair-software.nl/recommendations/repository) website lays out some of the options and guides you towards",
             "using `git` as your version control system.")
    st.write("The source code for this website is available in a [public GitHub repository](https://github.com/murphyqm/derelict), using the `git` version control system.")

with tab3:
    st.header("License: add one to your repository!")
    st.write("By default, your software is copyrighted, which means that legally, others cannot isntall and run your code.",
             "You want people to use your code! You also probably want to be recognised as the author of it, want to ensure",
             "you are not liable if it breaks and produces bad results for someone, and might have different requirements",
             "from your funder, research institute, or employer on what licenses you can use.")
    st.caption("Disclaimer: This guide is intended to list resources which may be useful to those sharing research code and is not legal advice. The author is not responsible for the content referenced in this guide.")
    st.write("Find out more in this [blog post](https://www.software.ac.uk/guide/choosing-open-source-licence) from the Software Sustainability Institute.")
    st.subheader("1. Ask for guidance from your employer or funding body")
    st.write("Many funding bodies and universities now have policies and guidance on licenses to use for datasets and software associated",
             "with research work. Check to see if your employer has any requirements or guidance for picking a software license.",
             "Your university's library staff may also be a good port of call, directing you to the appropriate bodies to seek advice and approval from.")
    st.subheader("2. Look at popular commonly used licenses")
    st.write("There are many different resources available to help you choose a license for your code, such as [choosealicense.com](https://choosealicense.com/).",
             "You can also see what other open source projects use by checking their license files within their repositories.")
    st.divider()
    st.write("For example, the repository for this webpage uses the 'MIT License', which can be found in the [GitHub repository](https://github.com/murphyqm/derelict/blob/main/LICENSE).",
             "This is a simple open source license, with the following text:")
    license_text = '''
    MIT License

    Copyright (c) 2024 Maeve Murphy Quinlan

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    '''
    st.code(license_text, language="markdown")

with tab4:
    st.header("Citation: make it easy!")
    st.write("Once you have published your code in a repository, and have included a license that allows re-use, you will want to",
             "make it as easy as possible for people to correctly attribute your work to you.",
             "Citing software can be a bit less straightforward than for journal articles, so you want to ensure",
             "users (including yourself) can accurately and easily cite specific versions of your code.")
    st.write("There are two parts to this: firstly, making sure that your code implements a versioning method, and secondly, including a citation file for users to reference.")
    st.subheader("1. Versioning your code")
    st.write("You should implement some form of versioning in your code, such as [Semantic Versioning](https://semver.org/), so that",
             "you can easily refer to a specific versionin of your code. On a smaller scale, this can be done if you use `git` as a version control system,",
             "by simply referencing a specific `git commit` unique ID; however, this can quickly become very messy and confusing.",
             "More formally, you can 'release' a new version of your code with a semantic version number like 1.0.2",
             "and even tie this new version to a Digital Object Identifier (DOI).")
    st.write("GitHub provides extensive documentation on how to",
             "[create a new release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)",
             "and how to issue a [DOI for the release](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).")
    st.write("This allows you to properly cite your own code when submitting a journal article that uses the code, and will provide a",
             "framework for other users going forward to properly acknowledge your code when they use it.")
    st.subheader("2. Include a citation file")
    st.write("A citation file is simply a text file that tells users of the code how to correctly cite the software.",
             "This could simply be a plain text file in your code repository that says 'Please cite this code as...'",
             "or it could be a human- and machine-readable ['Citation File Format'](https://citation-file-format.github.io/) file.",
             "You can update this citation file to match the version of code in the repository (so the most recent release).",
             "GitHub also gives [guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)",
             "on adding citation files to your repository.")

with tab5:
    st.header("Test your code!")
    st.write("In the same way you would set up validation and checks on lab analysis of samples via primary and secondary standards,",
             "so too should you test and benchmark your code."
             "Separate from validating numerical models against analytical results, or larger-scale research validation,",
             "code should be tested at a granular level with simple, toy data sets.",
             "This [documentation page](https://best-practice-and-impact.github.io/qa-of-code-guidance/testing_code.html) provides a useful",
             "introduction and simple tutorial to validating and testing code in both R and Python. Regardless of the language",
             "you use, the concepts and methods explained in this tutorial are applicable and useful for developing your own test suite.")
    st.write(
        "Of course, you can take things a step further and start to work using a",
        "[Test driven development](https://en.wikipedia.org/wiki/Test-driven_development) workflow,",
        "and develop an [authomated test suite](https://docs.github.com/en/actions/automating-builds-and-tests) in GitHub to run when any change is made to the code."
    )
    st.write("Having robust tests in place, alongside a version control system, means that you can be sure that you won't unknowingly incorporate and",
             "propagate an error in your code when you are extending and updating your software.",
             "It also makes it much easier to review any changes or contributions to the code suggested by collaborators.")
    st.write("Using your version control system, you can ensure that only code that passes your test suite is merged with [the main or production branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches),",
             "so users and collaborators never download a buggy new update.")