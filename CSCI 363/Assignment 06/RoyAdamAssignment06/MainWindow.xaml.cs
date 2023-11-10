using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace RoyAdamAssignment06
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private bool _editMode;
        public MainWindow()
        {
            InitializeComponent();

            RegionSelector.SelectedIndex = 0;
            NumberFormat.SelectedIndex = 0;
            CurrencyFormat.SelectedIndex = 0;
            TimeFormat.SelectedIndex = 0;
            DateFormat.SelectedIndex = 0;

            NumberBox.IsReadOnly = true;
            TimeBox.IsReadOnly = true;
            ShortDateBox.IsReadOnly = true;
            LongDateBox.IsReadOnly = true;
            CurrencyBox.IsReadOnly = true;

            RegionSelector.IsEnabled = false;
            NumberFormat.IsEnabled = false;
            CurrencyFormat.IsEnabled = false;
            TimeFormat.IsEnabled = false;
            DateFormat.IsEnabled = false;

            NumberBox.IsEnabled = false;
            TimeBox.IsEnabled = false;
            ShortDateBox.IsEnabled = false;
            LongDateBox.IsEnabled = false;
            CurrencyBox.IsEnabled = false;
        }

        public void ChangeFormatButton_Click(object sender, RoutedEventArgs e)
        {
            _editMode = !_editMode;
            if (_editMode)
            {
                ChangeFormatButton.Content = "Change Format";

                RegionSelector.IsEnabled = false;
                NumberFormat.IsEnabled = false;
                CurrencyFormat.IsEnabled = false;
                TimeFormat.IsEnabled = false;
                DateFormat.IsEnabled = false;

                NumberBox.IsEnabled = false;
                TimeBox.IsEnabled = false;
                ShortDateBox.IsEnabled = false;
                LongDateBox.IsEnabled = false;
                CurrencyBox.IsEnabled = false;
            }
            else
            {
                ChangeFormatButton.Content = "Submit";

                RegionSelector.IsEnabled = true;
                NumberFormat.IsEnabled = true;
                CurrencyFormat.IsEnabled= true;
                TimeFormat.IsEnabled= true;
                DateFormat.IsEnabled = true;

                NumberBox.IsEnabled = true;
                TimeBox.IsEnabled= true;
                ShortDateBox.IsEnabled = true;
                LongDateBox.IsEnabled = true;
                CurrencyBox.IsEnabled = true;
            }
        }
    }
}
