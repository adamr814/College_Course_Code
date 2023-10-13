using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace RoyAdamAssignment03
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public List<Department> departments;
        public MainWindow()
        {
            InitializeComponent();

            var department1 = new Department();
            department1.Name = "Computer Science";
            department1.Courses.Add(new Course { Name = "CSCI130" });
            department1.Courses.Add(new Course { Name = "CSCI160" });
            department1.Courses.Add(new Course { Name = "CSCI161" });
            department1.Courses.Add(new Course { Name = "CSCI242" });
            department1.Courses.Add(new Course { Name = "CSCI265" });
            department1.Courses.Add(new Course { Name = "CSCI266" });
            department1.Courses.Add(new Course { Name = "CSCI280" });
            department1.Courses.Add(new Course { Name = "CSCI289" });
            department1.Courses.Add(new Course { Name = "CSCI327" });
            department1.Courses.Add(new Course { Name = "CSCI330" });
            department1.Courses.Add(new Course { Name = "CSCI363" });
            department1.Courses.Add(new Course { Name = "CSCI364" });
            department1.Courses.Add(new Course { Name = "CSCI365" });
            department1.Courses.Add(new Course { Name = "CSCI370" });
            department1.Courses.Add(new Course { Name = "CSCI435" });
            department1.Courses.Add(new Course { Name = "CSCI451" });
            department1.Courses.Add(new Course { Name = "CSCI455" });
            department1.Courses.Add(new Course { Name = "CSCI463" });
            department1.Courses.Add(new Course { Name = "CSCI492" });
            department1.Courses.Add(new Course { Name = "CSCI493" });

            var department2 = new Department();
            department2.Name = "Mathematics";
            department2.Courses.Add(new Course { Name = "MATH165" });
            department2.Courses.Add(new Course { Name = "MATH166" });
            department2.Courses.Add(new Course { Name = "MATH207" });
            department2.Courses.Add(new Course { Name = "MATH208" });
            department2.Courses.Add(new Course { Name = "MATH265" });
            department2.Courses.Add(new Course { Name = "MATH266" });
            department2.Courses.Add(new Course { Name = "MATH330" });
            department2.Courses.Add(new Course { Name = "MATH488" });

            var department3 = new Department();
            department3.Name = "Electrical Engineering";
            department3.Courses.Add(new Course { Name = "EE201" });
            department3.Courses.Add(new Course { Name = "EE201L" });

            var department4 = new Department();
            department4.Name = "Accounting";
            department4.Courses.Add(new Course { Name = "ACCT200" });
            department4.Courses.Add(new Course { Name = "ACCT201" });


            departments = new List<Department> { department1, department2, department3, department4 };
            CourseTree.ItemsSource = departments;
        }
        //checks if there are existing students or courses when adding to the treeview
        private HashSet<string> existingStudentNames = new HashSet<string>();
        private HashSet<string> existingCourses = new HashSet<string>();

        
        private void CourseTree_SelectedItemChanged(object sender, RoutedPropertyChangedEventArgs<object> e)
        {
            if (e.NewValue is Course selectedCourse)
            {
                SelectedCourseTextBox.Text = selectedCourse.Name;
            }
        }

        private void ClearSelectionButton_Click(object sender, RoutedEventArgs e)
        {
            SelectedCourseTextBox.Text = "";
            NameTextBox.Text = "";
            IDTextBox.Text = "";
            OptionSelect.SelectedIndex = 0;
        }

        //watches the submit button and chooses an action based on the dropdown menu
        private void SubmitButton_Click(object sender, RoutedEventArgs e)
        {
            int selectedIndex = OptionSelect.SelectedIndex;

            string id = IDTextBox.Text;
            string studentName = NameTextBox.Text;
            string selectedCourse = SelectedCourseTextBox.Text;
            TreeViewItem? idNode = null;
            switch (selectedIndex)
            {
                case 0:
                    break;

                case 1:
                    idNode = FindOrCreateParentNode(StudentRecords, id);
                    if (idNode != null)
                    {
                        if (!existingStudentNames.Contains(studentName))
                        {
                            existingStudentNames.Add(studentName);
                            TreeViewItem nameNode = new TreeViewItem { Header = studentName };
                            idNode.Items.Add(nameNode);
                        }
                        if (!existingCourses.Contains(selectedCourse))
                        {
                            existingCourses.Add(selectedCourse);
                            TreeViewItem courseNode = new TreeViewItem { Header = selectedCourse };
                            idNode.Items.Add(courseNode);
                        }
                    }
                    break;

                case 2:
                    if(idNode != null)
                    {
                        TreeViewItem? courseToRemove = null;
                        foreach (TreeViewItem childNode in idNode.Items)
                        {
                            if (childNode.Header.ToString() == selectedCourse)
                            {
                                courseToRemove = childNode;
                                break;
                            }
                        }
                        if(courseToRemove != null)
                        {
                            idNode.Items.Remove(courseToRemove);
                        }
                        else
                        {
                            MessageBox.Show("Course not found or couldn't be removed.", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                        }
                    }                   
                    break;
            }
        }
        
        private TreeViewItem FindOrCreateParentNode(TreeView treeView, string key)
        {
            foreach (var node in treeView.Items) 
            { 
                if(node is TreeViewItem item && item.Header.ToString() == key)
                {
                    return item;
                }
            }
            
            var newNode = new TreeViewItem { Header = key };
            treeView.Items.Add(newNode);
            return newNode;
        }
    }
}


