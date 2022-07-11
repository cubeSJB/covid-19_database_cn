using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net;
using System.Net.Sockets;
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

namespace WPFapp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        int sendLength = 1024;
        Connection connection = new Connection();
        public MainWindow()
        {
            InitializeComponent();
            DataTable Table = new DataTable();
            Grid.ItemsSource = Table.DefaultView;
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                connection = new Connection(Server.Text, 8000);
                DataTable datatable = new DataTable();
                if (connection.AccoutRegister(Id.Text, Password.Password) == false)
                {
                    MessageBox.Show("请重新输入");
                    return;
                }
                else
                {
                    MessageBox.Show("已注册");
                }
                connection.Close();
                return;
            }
            catch (SocketException)
            {
                MessageBox.Show("连接意外断开");
                return;
            }
        }

        private void QnP_Click(object sender, RoutedEventArgs e)
        {
            connection.QueryInformation(0, QDate.Text, QPosition.Text);

        }

        private void Login_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                connection = new Connection(Server.Text, 8000);
                DataTable datatable = new DataTable();
                if (connection.AccoutLogin(Id.Text, Password.Password) == false)
                {
                    MessageBox.Show("请重新输入");
                    return;
                }
                database Dbs = new database(connection);
                Dbs.Show(this);
                return;
            }
            catch (SocketException)
            {
                MessageBox.Show("无法连接到服务器");
                return;
            }
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            Environment.Exit(0);
        }
    }
    public class ShowInfomation
    {
        public ShowInfomation() { }
        public bool instanceStatus;
        public char GetStat;
        public int Length;
        char QueryType;
        public bool DataType = false;

        public DataTable table = new DataTable("查询疫情数据");


        public static bool IsVirusData(char QueryType)
        {
            List<char> list = new List<char>()
            {
                '0',
                '1',
                '2',
                '6',
                '7',
                '8'
            };

            if (list.Contains(QueryType)) { return true; }
            return false;
        }

        public ShowInfomation(String S)
        {
            if (S[0] == 'Q' || S[0] == 'L' || S[0] == 'D' || S[0] == 'A' || S[0] == 'S')
            {
                string[] strings = S.Split(',');
                GetStat = strings[0][0];
                if (GetStat != 'Q')
                {
                    return;
                }
                else
                {

                    Length = Convert.ToInt32(strings[2]);
                    QueryType = strings[1][0];

                    if (IsVirusData(QueryType))
                    {
                        DataType = true;
                        table.Columns.Add("日期", typeof(string));
                        table.Columns.Add("地区", typeof(string));
                        table.Columns.Add("总疑似数", typeof(Int32));
                        table.Columns.Add("总感染数", typeof(Int32));
                        table.Columns.Add("总治愈数", typeof(Int32));
                        table.Columns.Add("总死亡数", typeof(Int32));
                        table.Columns.Add("新增疑似数", typeof(Int32));
                        table.Columns.Add("新增感染数", typeof(Int32));
                        table.Columns.Add("新增治愈数", typeof(Int32));
                        table.Columns.Add("新增死亡数", typeof(Int32));

                        for (int i = 0; i < Length; i++)
                        {
                            DataRow dr = table.NewRow();
                            dr["日期"] = strings[3 + i * 10];
                            dr["地区"] = strings[4 + i * 10];
                            dr["总疑似数"] = Convert.ToInt32(strings[5 + i * 10]);
                            dr["总感染数"] = Convert.ToInt32(strings[6 + i * 10]);
                            dr["总治愈数"] = Convert.ToInt32(strings[7 + i * 10]);
                            dr["总死亡数"] = Convert.ToInt32(strings[8 + i * 10]);
                            dr["新增疑似数"] = Convert.ToInt32(strings[9 + i * 10]);
                            dr["新增感染数"] = Convert.ToInt32(strings[10 + i * 10]);
                            dr["新增治愈数"] = Convert.ToInt32(strings[11 + i * 10]);
                            dr["新增死亡数"] = Convert.ToInt32(strings[12 + i * 10]);
                            table.Rows.Add(dr);
                        }
                    }
                }
                instanceStatus = true;
            }
            else
            {
                instanceStatus = false;
                return;
            }
        }

    }

    public class Connection
    {
        public IPEndPoint ipe = new IPEndPoint(0, 8000);
        public Socket tempSocket = new Socket(new IPEndPoint(0, 8000).AddressFamily, SocketType.Stream, ProtocolType.Tcp);

        public ShowInfomation information = new ShowInfomation();
        public void Close()
        {
            try
            {
                byte[] Rbyte = new byte[1024];
                string SocketString = "S";
                byte[] InsertBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(InsertBytes);
                tempSocket.Close();
            }
            catch
            {
                ;
            }
        }

        public Connection() { }

        public Connection(string Domain, int Port)
        {
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Domain);
            IPAddress myip = ipHostInfo.AddressList[0];
            ipe = new IPEndPoint(myip, Port);
            tempSocket = new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            tempSocket.Connect(ipe);
        }

        public bool AccoutLogin(string Accout, string Password)
        {
            byte[] Rbyte = new byte[2048];
            string SocketString = "L," + Accout;
            SocketString += ",";
            SocketString += Password;

            byte[] InsertBytes = Encoding.UTF8.GetBytes(SocketString);
            tempSocket.Send(InsertBytes);
            tempSocket.Receive(Rbyte);
            string Return = Encoding.UTF8.GetString(Rbyte);
            ShowInfomation Iinformation = new ShowInfomation(Return);
            if (Iinformation.GetStat == 'L')
            {
                return true;
            }
            else if (Iinformation.GetStat == 'R')
            {
                return false;
            }
            return false;
        }

        public bool AccoutRegister(string Accout, string Password)
        {
            byte[] Rbyte = new byte[2048];
            string SocketString = "C," + Accout;
            SocketString += ",";
            SocketString += Password;

            byte[] InsertBytes = Encoding.UTF8.GetBytes(SocketString);
            tempSocket.Send(InsertBytes);
            tempSocket.Receive(Rbyte);
            string Return = Encoding.UTF8.GetString(Rbyte);
            ShowInfomation Iinformation = new ShowInfomation(Return);
            if (Iinformation.GetStat == 'F')
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        public void InsertInformation(string Date, string Name, int Suspected, int Add, int Cured, int Dead)
        {
            try
            {
                byte[] Rbyte = new byte[2048];

                string SocketString = "I,";
                SocketString += DateFormat(Date);
                SocketString += Name + ',';
                SocketString += Suspected.ToString() + ',';
                SocketString += Add.ToString() + ',';
                SocketString += Cured.ToString() + ',';
                SocketString += Dead.ToString();

                byte[] InsertBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(InsertBytes);
                tempSocket.Receive(Rbyte);
                string Return = Encoding.UTF8.GetString(Rbyte);

                information = new ShowInfomation(Return);

                if (information.GetStat == 'N')
                {
                    throw new MessageError();
                }
            }
            catch
            {
                throw new ServerConnectionException();
            }
        }
        public void QueryInformation(int Option, string Date, string Name)
        {
            try
            {
                byte[] Qbyte = new byte[4194304];

                string SocketString = "Q,";
                SocketString += Option.ToString() + ',';
                SocketString += DateFormat(Date);
                SocketString += Name;

                byte[] QueryBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(QueryBytes);
                tempSocket.Receive(Qbyte);
                string Return = Encoding.UTF8.GetString(Qbyte);

                int lastIndex = Return.LastIndexOf('Q');

                string FinalStr = Return.Substring(lastIndex);

                information = new ShowInfomation(FinalStr);
            }
            catch (SocketException)
            { MessageBox.Show("服务器连接出现问题!"); }
            catch { MessageBox.Show("出现问题"); }
        }
        public bool DeleteInformation(int Option, string Date, string Name)
        {
            try
            {
                byte[] Dbyte = new byte[1024];

                string SocketString = "D,";
                SocketString += Option.ToString() + ',';
                SocketString += DateFormat(Date);
                SocketString += Name;

                byte[] DeleteBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(DeleteBytes);
                tempSocket.Receive(Dbyte);
                string Return = Encoding.UTF8.GetString(Dbyte);

                information = new ShowInfomation(Return);
                if (information.GetStat == 'Y')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch
            {
                return false;
            }
        }
        public bool DeleteInformation(int Option, string Name)
        {
            try
            {
                byte[] Dbyte = new byte[1024];

                string SocketString = "D,";
                SocketString += Option.ToString() + ",,";
                SocketString += Name;

                byte[] DeleteBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(DeleteBytes);
                tempSocket.Receive(Dbyte);
                string Return = Encoding.UTF8.GetString(Dbyte);

                information = new ShowInfomation(Return);
                if (information.GetStat == 'Y')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch
            {
                return false;
            }
        }
        public bool AlterInformation(string Date, string Name, int Add, int Cured, int Suspected, int Dead)
        {
            try
            {
                byte[] Abyte = new byte[1024];

                string SocketString = "A,";
                SocketString += DateFormat(Date);
                SocketString += Name + ',';
                SocketString += Add.ToString() + ',';
                SocketString += Cured.ToString() + ',';
                SocketString += Suspected.ToString() + ',';
                SocketString += Dead.ToString();

                byte[] InsertBytes = Encoding.UTF8.GetBytes(SocketString);
                tempSocket.Send(InsertBytes);
                tempSocket.Receive(Abyte);
                string Return = Encoding.UTF8.GetString(Abyte);

                information = new ShowInfomation(Return);

                if (information.GetStat == 'Y')
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch
            {
                return false;
            }
        }
        public void ShutConnection()
        {
            tempSocket.Close();
        }
        public static string DateFormat(string Ostring)
        {
            string Date = "";

            Date += Ostring.Split('/')[0];
            Date += '-';
            if (Ostring.Split('/')[1].Length == 1)

            {
                Date += "0";
                Date += Ostring.Split('/')[1];
            }
            else
            {
                Date += Ostring.Split('/')[1];
            }

            Date += '-';
            if (Ostring.Split('/')[2].Length == 1)
            {
                Date += "0";
                Date += Ostring.Split('/')[2];
            }
            else
            {
                Date += Ostring.Split('/')[2];
            }

            Date += ',';
            return Date;
        }
    }
    public class ServerConnectionException : Exception { }
    public class MessageError : Exception { }
}
