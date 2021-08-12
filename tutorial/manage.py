#!/usr/bin/env python
"""
프로젝트 관리 명령어 모음
    startapp - 앱 생성
    runserver - 서버 실행
    createsuperuser - 관리자 생성
    makemigrations app - app의 모델 변경 사항 체크
    migrate - 변경 사항을 db에 반영
    shell - 쉘을 통해 데이터를 확인
    collectstatic - static파일을 한 곳에 모음
"""

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
