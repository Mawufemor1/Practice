#include <iostream> 
using namespace std;
int main() 
{
    double grade = 0;
    double average_Grade = 0;
    int sum_grades = 0;
    int num_Students = 0; 
    int num_pass = 0;
    int num_fail = 0;
    int max_grade = 0;
    int min_grade = 0;
    int temp_max = 0;
    int temp_min = 0;
    int decimal = 0;


    cout << "Enter the students mark and If you want to stop inputing grades type 1000" << endl;
    
    while( num_Students != 30) {
      cout << "Input marks: ";
      cin >> grade;
      if (grade == 1000)
      {break;}

      decimal = static_cast<int>(grade);
      if(decimal != grade || grade > 100 || grade < 0) {
        cout << "The marks can not be decimals and they should range from 0 to 100. Try again!" << endl;
      }
      else{
        num_Students++;
        if (num_Students == 1){
          temp_max = grade;
          temp_min = grade;
        }

        sum_grades += grade;
        average_Grade = sum_grades / num_Students;

        if (grade > temp_max){
          temp_max = grade;
        }
        if (grade < temp_min){
        temp_min = grade;
        }

        if (grade >= 60){
          num_pass++;
        }
        else{
          num_fail++;
        }

      }


    }

    max_grade = temp_max;
    min_grade = temp_min;


    cout << "The highest grade is " << max_grade << "%" << endl;
    cout << "The lowest grade is " << min_grade << "%" << endl;
    cout << "The average grade is " << average_Grade << "%" << endl;
    cout << "Number of students who passed: " << num_pass << endl;
    cout << "Number of students who failed: " << num_fail << endl;
  

    return 0;
}