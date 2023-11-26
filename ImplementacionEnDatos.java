import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PublicKey;
import java.util.Base64;
import java.util.Random;

import javax.crypto.Cipher;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class Trabajador {
    private JTextField nombreCompletoField;
    private JTextField documentoIdentidadField;
    private JTextField correoField;
    private JTextField telefonoField;
    private JTextField codeField;
    private JTextArea infoArea;
    private String storedEncryptedData;
    private KeyPair keyPair;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Trabajador trabajador = new Trabajador();
            trabajador.createAndShowGUI();
        });
    }

    public void createAndShowGUI() {
        JFrame frame = new JFrame("Sistema de Trabajador");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(0, 2));

        frame.add(new JLabel("Nombre completo del trabajador:"));
        nombreCompletoField = new JTextField();
        frame.add(nombreCompletoField);

        frame.add(new JLabel("Documento de identidad:"));
        documentoIdentidadField = new JTextField();
        frame.add(documentoIdentidadField);

        frame.add(new JLabel("Correo electronico:"));
        correoField = new JTextField();
        frame.add(correoField);

        frame.add(new JLabel("Numero de telefono:"));
        telefonoField = new JTextField();
        frame.add(telefonoField);

        frame.add(new JLabel("Codigo de acceso:"));
        codeField = new JTextField();
        frame.add(codeField).setEnabled(false);

        JButton encryptButton = new JButton("Encriptar");
        frame.add(encryptButton);

        encryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String nombreCompleto = nombreCompletoField.getText();
                String documentoIdentidad = documentoIdentidadField.getText();
                String correo = correoField.getText();
                String telefono = telefonoField.getText();

                String datos = nombreCompleto + ";" + documentoIdentidad + ";" + correo + ";" + telefono;
                try {
                    KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
                    keyPairGenerator.initialize(2048);
                    keyPair = keyPairGenerator.generateKeyPair();
                    PublicKey publicKey = keyPair.getPublic();
                    String encryptedData = RSAUtil.encrypt(datos, publicKey);

                    // CODIGO GENERADO
                    String code = generateEightDigitCode();
                    codeField.setText(code);

                    // Simular el almacenamiento del codigo y los datos como si fuera en una base de
                    // datos
                    storedEncryptedData = encryptedData;

                    infoArea.setText("Datos encriptados y guardados con éxito.");
                } catch (Exception ex) {
                    infoArea.setText("Error al encriptar y guardar los datos.");
                }

                nombreCompletoField.setEnabled(false);
                documentoIdentidadField.setEnabled(false);
                correoField.setEnabled(false);
                telefonoField.setEnabled(false);
                encryptButton.setEnabled(false);
                codeField.setEnabled(false);

            }
        });

        JButton verifyCodeButton = new JButton("Verificar Código");
        frame.add(verifyCodeButton);

        verifyCodeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFrame codeVerificationFrame = new JFrame("Verificación de Código");
                JTextField codeVerificationField = new JTextField();
                JButton checkCodeButton = new JButton("Verificar");

                codeVerificationFrame.setLayout(new GridLayout(0, 1));
                codeVerificationFrame.add(new JLabel("Ingrese el código:"));
                codeVerificationFrame.add(codeVerificationField);
                codeVerificationFrame.add(checkCodeButton);

                checkCodeButton.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        String enteredCode = codeVerificationField.getText();
                        String storedCode = codeField.getText();

                        if (enteredCode.equals(storedCode)) {
                            try {
                                String decryptedData = RSAUtil.decrypt(storedEncryptedData, keyPair.getPrivate());
                                String[] decryptedFields = decryptedData.split(";");
                                String infoMessage = "Nombre: " + decryptedFields[0] + "\n" +
                                        "Documento: " + decryptedFields[1] + "\n" +
                                        "Correo: " + decryptedFields[2] + "\n" +
                                        "Teléfono: " + decryptedFields[3];
                                JOptionPane.showMessageDialog(null, infoMessage, "Datos desencriptados",
                                        JOptionPane.INFORMATION_MESSAGE);
                            } catch (Exception ex) {
                                JOptionPane.showMessageDialog(null, "Error al desencriptar los datos", "Error",
                                        JOptionPane.ERROR_MESSAGE);
                            }
                        } else {
                            JOptionPane.showMessageDialog(null, "Código incorrecto", "Error",
                                    JOptionPane.ERROR_MESSAGE);
                        }
                        codeVerificationFrame.dispose();
                    }
                });

                codeVerificationFrame.pack();
                codeVerificationFrame.setVisible(true);
            }
        });

        infoArea = new JTextArea();
        infoArea.setEditable(false);
        frame.add(infoArea);

        frame.pack();
        frame.setVisible(true);

    }

    private static String generateEightDigitCode() {
        Random random = new Random();
        int code = random.nextInt(90000000) + 10000000; // Rango de 10000000 a 99999999
        return String.valueOf(code);
    }
}

class RSAUtil {
     /// ENCRIPTAR
    public static String encrypt(String data, PublicKey publicKey) throws Exception {
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = cipher.doFinal(data.getBytes());
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }
    /// DESENCRIPTAR
    public static String decrypt(String data, java.security.PrivateKey privateKey) throws Exception {
        byte[] bytes = Base64.getDecoder().decode(data);
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(bytes);
        return new String(decryptedBytes);
    }
}
