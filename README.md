<div align="center">
<h1><a href="https://github.com/IHosseini/Shortify"><b>URL-Shortener</b></a></h1>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python">
</a>
<a href="https://github.com/psf/black">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat" alt="Code Style: black">
</a>
<a href="https://github.com/pre-commit/mirrors-mypy">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=mypy&color=blue&style=flat" alt="Code Style: mypy">
</a>
<a href="https://github.com/pycqa/isort">
    <img src="https://img.shields.io/static/v1?label=code%20style&message=isort&color=yellow&style=flat" alt="Code Style: isort">
</a>
<a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat" alt="pre-commit">
</a>
<a href="https://github.com/tiangolo/fastapi">
    <img src="https://img.shields.io/badge/framework-fastapi-green" alt="pre-commit">
</a>
<a href="https://pypi.org/project/pipenv/">
    <img src="https://img.shields.io/badge/version--control-pipenv-darkgray" alt="pipenv">
</a>
<img src="https://img.shields.io/badge/build-docker-blue" alt="docker">
<a href="https://github.com/ihor-voronin/url-shortener/actions/workflows/ci.yml">
    <img src="https://github.com/ihor-voronin/url-shortener/actions/workflows/ci.yml/badge.svg?branch=release" alt="pipenv">
</a>
</div>

<details><summary>Docker version</summary>

```shell 
$ docker version
Client: Docker Engine - Community
 Version:           24.0.2
 API version:       1.43
 Go version:        go1.20.4
 Git commit:        cb74dfc
 Built:             Thu May 25 21:52:22 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.2
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.4
  Git commit:       659604f
  Built:            Thu May 25 21:52:22 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.21
  GitCommit:        3dce8eb055cbb6872793272b4f20ed16117344f8
 runc:
  Version:          1.1.7
  GitCommit:        v1.1.7-0-g860f061
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```
</details>

<details open><summary>API</summary>

```shell 
curl -X POST -d '{"url": "https://google.com"}' -H "Content-Type: application/json" http://localhost:8000/api/shorten
```
Response example:
``{"short_url":"Ns2GO5y"}``

```shell 
curl -X GET -Ls -o /dev/null -w %{url_effective} http://localhost:8000/Ns2GO5y
```
Redirect to: ``https://www.google.com/``

</details>
