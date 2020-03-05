//
// Created by linkinpark213 on 5/21/19.
//

#include <iostream>
#include <vector>

using namespace std;


class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;

    Employee(int id, int importance) : id(id), importance(importance) {};

    void addSubordinate(int i) {
        this->subordinates.push_back(i);
    }
};

class Solution {
public:
    int getImportance(vector<Employee *> employees, int id) {
        Employee *employee = NULL;
        for (auto &i : employees) {
            if (i->id == id) {
                employee = i;
            }
        }
        if (employee == NULL) return 0;
        int importance = employee->importance;
        for (auto &i: employee->subordinates) {
            importance += getImportance(employees, i);
        }
        return importance;
    }
};

int main() {
    Solution solution;
    Employee *employee1 = new Employee(1, 5);
    Employee *employee2 = new Employee(2, 3);
    Employee *employee3 = new Employee(3, 3);
    employee1->addSubordinate(2);
    employee1->addSubordinate(3);
    vector<Employee *> employees;
    employees.push_back(employee1);
    employees.push_back(employee2);
    employees.push_back(employee3);
    cout << solution.getImportance(employees, 1);
    return 0;
}