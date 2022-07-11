using static vDB.Login;

namespace vDB
{
    public partial class database : Form
    {
        public Connection connection;
        public database(Connection connect)
        {
            this.connection = connect;

            InitializeComponent();
        }

        private void CoQ_Click(object sender, EventArgs e)
        {
            switch (QType.SelectedIndex)
            {
                case 2:
                    connection.QueryInformation(3, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 3:
                case 0:
                case 1:
                    MessageBox.Show("无县级疫情信息！");
                    break;
            }
        }
        private void CQ_Click(object sender, EventArgs e)
        {
            switch (QType.SelectedIndex)
            {
                case 0:
                    connection.QueryInformation(0, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 1:
                    connection.QueryInformation(2, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 2:
                    connection.QueryInformation(4, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 3:
                    connection.QueryInformation(7, Sdate.Text, Qsite.Text, dataGrid);
                    break;
            }
        }
        private void PQ_Click(object sender, EventArgs e)
        {
            switch (QType.SelectedIndex)
            {
                case 0:
                    connection.QueryInformation(1, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 1:
                    connection.QueryInformation(6, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 2:
                    connection.QueryInformation(5, Sdate.Text, Qsite.Text, dataGrid);
                    break;
                case 3:
                    connection.QueryInformation(8, Sdate.Text, Qsite.Text, dataGrid);
                    break;
            }
        }
        private void Submit_Click(object sender, EventArgs e)
        {
            try
            {
                int Con = Convert.ToInt32(ConfirmSum.Text);
                int Cur = Convert.ToInt32(CuredSum.Text);
                int Sus = Convert.ToInt32(SuspectSum.Text);
                int Dea = Convert.ToInt32(DeadSum.Text);
                connection.InsertInformation(Idate.Text, Iarea.Text, Con, Cur, Sus, Dea);
                MessageBox.Show("已完成操作");
            }
            catch (FormatException)
            {
                MessageBox.Show("数据输入错误!");
            }
            catch (ServerConnectionException)
            {
                MessageBox.Show("服务器连接出现问题!");
            }
            catch (MessageError)
            {
                MessageBox.Show("返回值不合法，请检查连接安全性并通知管理员!");
            }
        }

        private void Exit_Click(object sender, EventArgs e)
        {
            connection.Close();
            Application.ExitThread();
        }
        private void AExit_Click(object sender, EventArgs e)
        {
            connection.Close();
            Application.ExitThread();
        }
        private void QExit_Click(object sender, EventArgs e)
        {
            connection.Close();
            Application.ExitThread();
        }
        private void DExit_Click(object sender, EventArgs e)
        {
            connection.Close();
            Application.ExitThread();
        }

        private void Asubmit_Click(object sender, EventArgs e)
        {
            try
            {
                int Con = Convert.ToInt32(ConfirmSum.Text);
                int Cur = Convert.ToInt32(CuredSum.Text);
                int Sus = Convert.ToInt32(SuspectSum.Text);
                int Dea = Convert.ToInt32(DeadSum.Text);
                connection.AlterInformation(Cdate.Text, Iarea.Text, Con, Cur, Sus, Dea);
                MessageBox.Show("已完成操作");
            }
            catch (FormatException)
            {
                MessageBox.Show("数据输入错误!");
            }
            catch (ServerConnectionException)
            {
                MessageBox.Show("服务器连接出现问题!");
            }
            catch (MessageError)
            {
                MessageBox.Show("返回值不合法，请检查连接安全性并通知管理员!");
            }
        }

        private void Dco_Click(object sender, EventArgs e)
        {

        }

        private void DC_Click(object sender, EventArgs e)
        {
            switch (QType.SelectedIndex)
            {
                case 0:
                    connection.DeleteInformation(1, Ddate.Text, Qname.Text);
                    break;
                case 1:
                    connection.DeleteInformation(0, Ddate.Text, Qname.Text);
                    break;
            }
        }

        private void DP_Click(object sender, EventArgs e)
        {
            switch (QType.SelectedIndex)
            {
                case 0:
                    connection.DeleteInformation(3, Qname.Text);
                    break;
                case 1:
                    connection.DeleteInformation(2, Qname.Text);
                    break;
            }
        }
    }
}
