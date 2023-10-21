using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Permissions;
using System.Text;
using System.Threading.Tasks;
using System.Transactions;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace RoyAdamAssignment04
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        private void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            if (int.TryParse(LoanAmount.Text, out int loanamount) &&             
                double.TryParse(LoanInterest.Text, out double interestRate))
            {
                List<MonthlyDetail> monthlyDetails = new List<MonthlyDetail>();
                double principal = loanamount;
                double totalInterest = 0.0;
                double fixedPayment = 0.0;
                if (double.TryParse(LoanPeriod.Text, out double time))
                {
                    int selectedIndex = timeSelector.SelectedIndex;
                    if (selectedIndex == 1)
                    {
                        time *= 12;
                    }
                    double monthlyInterestRate = (interestRate / 12);
                    double monthlyPayment = principal * (monthlyInterestRate * Math.Pow(1 + monthlyInterestRate, time)) / (Math.Pow(1 + monthlyInterestRate, time) - 1);

                    for (int month = 1; month <= time; month++)
                    {
                        double monthlyInterest = principal * monthlyInterestRate;
                        double principalPayment = monthlyPayment - monthlyInterest;
                        double remainingBalance = principal - principalPayment;
                        totalInterest += monthlyInterest;

                        MonthlyDetail detail = new MonthlyDetail
                        {
                            Month = month,
                            MonthlyPayment = Math.Round(monthlyPayment, 2),
                            InterestAmount = Math.Round(monthlyInterest, 2),
                            RemainingBalance = Math.Round(remainingBalance, 2),
                        };
                        monthlyDetails.Add(detail);
                        principal = remainingBalance;
                    }
                }
                else if (double.TryParse(MonthlyPayment.Text, out fixedPayment))
                {
                    for (int month = 1; month <= time; month++)
                    {
                        double monthlyInterest = (principal * interestRate) / 12;
                        double monthlyPayment = fixedPayment;
                        double remainingBalance = principal - monthlyPayment;
                        totalInterest += monthlyInterest;

                        MonthlyDetail detail = new MonthlyDetail
                        {
                            Month = month,
                            MonthlyPayment = Math.Round(monthlyPayment, 2),
                            InterestAmount = Math.Round(monthlyInterest, 2),
                            RemainingBalance = Math.Round(remainingBalance, 2),
                        };
                        monthlyDetails.Add(detail);
                        principal = remainingBalance;
                    }
                }
                else
                {
                    TotalInterestTextBox.Text = "Please enter a vailid interest rate or fixed payment";
                    MonthlyDetailsGrid.ItemsSource = null;
                    return;
                }

                TotalInterestTextBox.Text = $"Total Interest: {totalInterest:C}";
                MonthlyDetailsGrid.ItemsSource = monthlyDetails;
            }
            else
            {
                TotalInterestTextBox.Text = "Please enter valid numeric values";
                MonthlyDetailsGrid.ItemsSource = null;
            }
        }
    }
}
