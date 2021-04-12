# !usr/bin/env bash
echo "Running flake8..."
#find ./server -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731
find ./users -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./holdhand -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./products -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./home -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./search -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./questionsandanswers -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
find ./checkout -name "*.py" -print0 | xargs -0 -n 1 flake8 --ignore=E501,E402,E731,E722,E117,F632,E741,W605,W504,F901
echo "End of execution flake8..."