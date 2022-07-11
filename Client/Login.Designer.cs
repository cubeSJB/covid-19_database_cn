namespace vDB
{
    partial class Login
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Log = new System.Windows.Forms.Button();
            this.Exit = new System.Windows.Forms.Button();
            this.maingroup = new System.Windows.Forms.GroupBox();
            this.register = new System.Windows.Forms.Button();
            this.password = new System.Windows.Forms.TextBox();
            this.id = new System.Windows.Forms.TextBox();
            this.server = new System.Windows.Forms.TextBox();
            this.lable_password = new System.Windows.Forms.Label();
            this.lable_id = new System.Windows.Forms.Label();
            this.lable_server = new System.Windows.Forms.Label();
            this.maingroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // Log
            // 
            this.Log.Location = new System.Drawing.Point(609, 65);
            this.Log.Margin = new System.Windows.Forms.Padding(4);
            this.Log.Name = "Log";
            this.Log.Size = new System.Drawing.Size(143, 44);
            this.Log.TabIndex = 0;
            this.Log.Text = "登录(L)";
            this.Log.UseVisualStyleBackColor = true;
            this.Log.Click += new System.EventHandler(this.Log_Click);
            // 
            // Exit
            // 
            this.Exit.Location = new System.Drawing.Point(609, 144);
            this.Exit.Margin = new System.Windows.Forms.Padding(4);
            this.Exit.Name = "Exit";
            this.Exit.Size = new System.Drawing.Size(143, 44);
            this.Exit.TabIndex = 1;
            this.Exit.Text = "退出(Esc)";
            this.Exit.UseVisualStyleBackColor = true;
            this.Exit.Click += new System.EventHandler(this.Exit_Click);
            // 
            // maingroup
            // 
            this.maingroup.Controls.Add(this.register);
            this.maingroup.Controls.Add(this.password);
            this.maingroup.Controls.Add(this.id);
            this.maingroup.Controls.Add(this.Exit);
            this.maingroup.Controls.Add(this.server);
            this.maingroup.Controls.Add(this.Log);
            this.maingroup.Controls.Add(this.lable_password);
            this.maingroup.Controls.Add(this.lable_id);
            this.maingroup.Controls.Add(this.lable_server);
            this.maingroup.Location = new System.Drawing.Point(41, 28);
            this.maingroup.Margin = new System.Windows.Forms.Padding(4);
            this.maingroup.Name = "maingroup";
            this.maingroup.Padding = new System.Windows.Forms.Padding(4);
            this.maingroup.Size = new System.Drawing.Size(822, 310);
            this.maingroup.TabIndex = 2;
            this.maingroup.TabStop = false;
            this.maingroup.Text = "服务器信息";
            // 
            // register
            // 
            this.register.Location = new System.Drawing.Point(609, 223);
            this.register.Margin = new System.Windows.Forms.Padding(4);
            this.register.Name = "register";
            this.register.Size = new System.Drawing.Size(143, 44);
            this.register.TabIndex = 3;
            this.register.Text = "注册(R)";
            this.register.UseVisualStyleBackColor = true;
            this.register.Click += new System.EventHandler(this.register_Click);
            // 
            // password
            // 
            this.password.Location = new System.Drawing.Point(210, 227);
            this.password.Margin = new System.Windows.Forms.Padding(4);
            this.password.Name = "password";
            this.password.PasswordChar = '*';
            this.password.Size = new System.Drawing.Size(339, 38);
            this.password.TabIndex = 5;
            // 
            // id
            // 
            this.id.Location = new System.Drawing.Point(210, 146);
            this.id.Margin = new System.Windows.Forms.Padding(4);
            this.id.Name = "id";
            this.id.Size = new System.Drawing.Size(339, 38);
            this.id.TabIndex = 4;
            this.id.Text = "cube";
            // 
            // server
            // 
            this.server.Location = new System.Drawing.Point(210, 65);
            this.server.Margin = new System.Windows.Forms.Padding(4);
            this.server.Name = "server";
            this.server.Size = new System.Drawing.Size(339, 38);
            this.server.TabIndex = 3;
            this.server.Text = "developer.ksei.top";
            // 
            // lable_password
            // 
            this.lable_password.AutoSize = true;
            this.lable_password.Location = new System.Drawing.Point(94, 227);
            this.lable_password.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lable_password.Name = "lable_password";
            this.lable_password.Size = new System.Drawing.Size(62, 31);
            this.lable_password.TabIndex = 2;
            this.lable_password.Text = "密码";
            // 
            // lable_id
            // 
            this.lable_id.AutoSize = true;
            this.lable_id.Location = new System.Drawing.Point(94, 150);
            this.lable_id.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lable_id.Name = "lable_id";
            this.lable_id.Size = new System.Drawing.Size(62, 31);
            this.lable_id.TabIndex = 1;
            this.lable_id.Text = "账号";
            // 
            // lable_server
            // 
            this.lable_server.AutoSize = true;
            this.lable_server.Location = new System.Drawing.Point(94, 72);
            this.lable_server.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lable_server.Name = "lable_server";
            this.lable_server.Size = new System.Drawing.Size(86, 31);
            this.lable_server.TabIndex = 0;
            this.lable_server.Text = "服务器";
            // 
            // Login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(14F, 31F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(921, 378);
            this.Controls.Add(this.maingroup);
            this.KeyPreview = true;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Login";
            this.Text = "Login";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Login_KeyDown);
            this.maingroup.ResumeLayout(false);
            this.maingroup.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private Button Log;
        private Button Exit;
        private GroupBox maingroup;
        private TextBox password;
        private TextBox id;
        private TextBox server;
        private Label lable_password;
        private Label lable_id;
        private Label lable_server;
        private Button register;
    }
}