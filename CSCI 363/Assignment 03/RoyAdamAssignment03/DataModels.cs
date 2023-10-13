using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Data;

namespace RoyAdamAssignment03
{
    public class Department
    {
        public string Name { get; set; } = "";
        public List<Course> Courses { get; set; } = new List<Course>();
        public bool IsSelected { get; set; }
    }

    public class Course
    {
        public string Name { get; set; } = "";
        public bool IsSelected { get; set; }
    }
}
