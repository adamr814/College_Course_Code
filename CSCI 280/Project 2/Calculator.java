//package SimpleCalculator;
import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

public class Calculator implements ActionListener{
    double number, answer;
    int calculation;
    JFrame f;
    Calculator(){
        buildGUI();
        addComponents();
        addActionEvent();}
    
    public void buildGUI(){
        f = new JFrame();
        f.setTitle("Calculator");
        f.setSize(300, 490);
        f.getContentPane().setLayout(null);
        f.setResizable(false);
        f.setLocationRelativeTo(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    JLabel label = new JLabel();
    JLabel name = new JLabel();
    JTextField textField = new JTextField();
    JButton b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, bAdd, bSub, bMul, bDiv, bEqu, bDot, bClr, bDel, bPNT;{
        b0 = new JButton("0");    
        b1 = new JButton("1");    
        b2 = new JButton("2");    
        b3 = new JButton("3");    
        b4 = new JButton("4");    
        b5 = new JButton("5");    
        b6 = new JButton("6");    
        b7 = new JButton("7");    
        b8 = new JButton("8");    
        b9 = new JButton("9");    
        bAdd = new JButton("+");  
        bSub = new JButton("-");  
        bMul = new JButton("*");  
        bDiv = new JButton("/");  
        bClr = new JButton ("CLR"); 
        bDot = new JButton(".");  
        bEqu = new JButton("=");  
        bDel = new JButton("DEL");
        bPNT = new JButton("+/-");
    }

    public void addComponents(){
        label.setBounds(250, 0, 50, 50);
        f.add(label);
        name.setBounds(10, 430, 200, 20);
        name.setFont(new Font("Calibri", Font.ITALIC, 10));
        name.setHorizontalAlignment(SwingConstants.LEFT);
        name.setText("Adam Roy | Project 2 | CSCI280");
        f.add(name);
        textField.setBounds(10, 40, 265, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        textField.setEditable(false);
        textField.setHorizontalAlignment(SwingConstants.RIGHT);
        f.add(textField);

        b7.setBounds(10, 170, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b7);

        b8.setBounds(80, 170, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b8);

        b9.setBounds(150, 170, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b9);

        b4.setBounds(10, 230, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b4);

        b5.setBounds(80, 230, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b5);

        b6.setBounds(150, 230, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b6);

        b1.setBounds(10, 290, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b1);

        b2.setBounds(80, 290, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b2);

        b3.setBounds(150, 290, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b3);

        b0.setBounds(10, 350, 130, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(b0);

        bDiv.setBounds(220, 110, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bDiv);

        bMul.setBounds(220, 170, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bMul);

        bSub.setBounds(220, 230, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bSub);
        
        bAdd.setBounds(220, 290, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bAdd);
        
        bDot.setBounds(150, 350, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bDot);

        bEqu.setBounds(220, 350, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bEqu);

        bClr.setBounds(80, 110, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bClr);

        bDel.setBounds(150, 110, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bDel);
    
        bPNT.setBounds(10, 110, 60, 40);
        textField.setFont(new Font("Arial", Font.BOLD, 20));
        f.add(bPNT);}

    public void addActionEvent(){
        bClr.addActionListener(this);
        bDel.addActionListener(this);
        bDiv.addActionListener(this);
        bMul.addActionListener(this);
        bSub.addActionListener(this);
        bAdd.addActionListener(this);
        b0.addActionListener(this);
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
        b7.addActionListener(this);
        b8.addActionListener(this);
        b9.addActionListener(this);
        bEqu.addActionListener(this);
        bDot.addActionListener(this);
        bPNT.addActionListener(this);}
    
        @Override
        public void actionPerformed(ActionEvent e){
            Object source = e.getSource();
            if(source==bClr){
                label.setText("");
                textField.setText("");}

            else if(source==bDel){
                int length = textField.getText().length();
                int number = length -1;
                if(length > 0){
                    StringBuilder back = new StringBuilder(textField.getText());
                    back.deleteCharAt(number);
                    textField.setText(back.toString());}
                if(textField.getText().endsWith("")){
                    label.setText("");}}

            else if(source==b0){
                if(textField.getText().equals("0")){
                    return;}
                else{
                    textField.setText(textField.getText() + "0");}}
            else if(source==b1){textField.setText(textField.getText() + "1");}
            else if(source==b2){textField.setText(textField.getText() + "2");}
            else if(source==b3){textField.setText(textField.getText() + "3");}
            else if(source==b4){textField.setText(textField.getText() + "4");}
            else if(source==b5){textField.setText(textField.getText() + "5");}
            else if(source==b6){textField.setText(textField.getText() + "6");}
            else if(source==b7){textField.setText(textField.getText() + "7");}
            else if(source==b8){textField.setText(textField.getText() + "8");}
            else if(source==b9){textField.setText(textField.getText() + "9");}
            else if(source==bDot){
                if(textField.getText().contains(".")){
                    return;}
                else{
                    textField.setText(textField.getText() + ".");}}
            else if(source==bPNT){
                number = Double.parseDouble(textField.getText());
                double negResult = number *= -1;
                textField.setText(negResult + "");}
            else if(source==bAdd){
                String str = textField.getText();
                number = Double.parseDouble(textField.getText());
                textField.setText("");
                label.setText(str + " + ");
                calculation = 1;}
            else if(source==bSub){
                String str = textField.getText();
                number = Double.parseDouble(textField.getText());
                textField.setText("");
                label.setText(str + " - ");
                calculation = 2;}
            else if(source==bMul){
                String str = textField.getText();
                number = Double.parseDouble(textField.getText());
                textField.setText("");
                label.setText(str + " X ");
                calculation = 3;}
            else if(source==bDiv){
                String str = textField.getText();
                number = Double.parseDouble(textField.getText());
                textField.setText("");
                label.setText(str + " / ");
                calculation = 4;}
            else if(source==bEqu){
                switch(calculation){
                    case 1:
                        answer = number + Double.parseDouble(textField.getText());
                        if(Double.toString(answer).endsWith(".0")){
                            textField.setText(Double.toString(answer).replace(".0", ""));}
                        else{
                            textField.setText(Double.toString(answer));}
                        label.setText("");
                        break;
                    case 2:
                        answer = number - Double.parseDouble(textField.getText());
                        if(Double.toString(answer).endsWith(".0")){
                            textField.setText(Double.toString(answer).replace(".0", ""));}
                        else{
                            textField.setText(Double.toString(answer));}
                        label.setText("");
                        break;
                    case 3:
                        answer = number * Double.parseDouble(textField.getText());
                        if(Double.toString(answer).endsWith(".0")){
                            textField.setText(Double.toString(answer).replace(".0", ""));}
                        else{
                            textField.setText(Double.toString(answer));}
                        label.setText("");
                        break;
                    case 4:
                        answer = number / Double.parseDouble(textField.getText());
                        if(Double.toString(answer).endsWith(".0")){
                            textField.setText(Double.toString(answer).replace(".0", ""));}
                        else{
                            textField.setText(Double.toString(answer));}
                        label.setText("");
                        break;}}}}