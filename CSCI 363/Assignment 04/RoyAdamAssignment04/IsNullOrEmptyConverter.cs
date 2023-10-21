using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Data;

namespace RoyAdamAssignment04
{
    public class IsNullOrEmptyConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string strValue)
            {
                return string.IsNullOrEmpty(strValue);
            }
            return true;
        }
        public object ConvertBack(object value, Type target, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }

    }
}
