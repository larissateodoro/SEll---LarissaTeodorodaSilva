#include "blocodenotas.h"
#include "ui_blocodenotas.h"
#include <QMessageBox>
#include <QFile>
#include <QFileDialog>
#include <QTextStream>

BlocoDeNotas::BlocoDeNotas(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::BlocoDeNotas)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->textEdit);
}

BlocoDeNotas::~BlocoDeNotas()
{
    delete ui;
}

void BlocoDeNotas::on_actionNovo_triggered()
{
    local_arquivo="";
    ui->textEdit->clear();
    ui->textEdit->setFocus();


}

void BlocoDeNotas::on_actionAbrir_triggered()
{
   QString filtro = "Arquivos de Texto (*.txt) ;; Todos Arquivos (*.*) ";
   QString nome_arquivo=QFileDialog::getOpenFileName(this,"Abrir",QDir::homePath(),filtro);
   QFile arquivo(nome_arquivo);
   local_arquivo= nome_arquivo;
   if(!arquivo.open(QFile::ReadOnly | QFile::Text)){
       QMessageBox::warning(this, "","Arquivo não pôde ser aberto");
       return;

   }
   QTextStream entrada (&arquivo);
   QString texto=entrada.readAll();
   ui->textEdit->setText(texto);
   arquivo.close();

}

void BlocoDeNotas::on_actionSalvar_Como_triggered()
{
    QString filtro = "Arquivos de Texto (*.txt) ;; Todos Arquivos (*.*) ";
    QString nome_arquivo=QFileDialog::getSaveFileName(this,"Salvar Como",QDir::homePath(),filtro);
    local_arquivo=nome_arquivo;
    QFile arquivo(nome_arquivo);
    if(!arquivo.open(QFile::WriteOnly | QFile::Text)){
        QMessageBox::warning(this, "","Arquivo não pôde ser salvo");
        return;

    }
    QTextStream saida (&arquivo);
    QString texto=ui->textEdit->toPlainText();
    saida << texto;
    arquivo.flush();
    arquivo.close();
}

void BlocoDeNotas::on_actionSalvar_triggered()
{

    QFile arquivo(local_arquivo);
    if(!arquivo.open(QFile::WriteOnly | QFile::Text)){
        QMessageBox::warning(this, "","Arquivo não pôde ser salvo");
        return;
    }
    QTextStream saida (&arquivo);
    QString texto=ui->textEdit->toPlainText();
    saida << texto;
    arquivo.flush();
    arquivo.close();
}

void BlocoDeNotas::on_actionFechar_triggered()
{
    close();
}

void BlocoDeNotas::on_actionRecortar_triggered()
{
    ui->textEdit->cut();
}

void BlocoDeNotas::on_actionCopiar_triggered()
{
    ui->textEdit->copy();
}

void BlocoDeNotas::on_actionColar_triggered()
{
    ui->textEdit->paste();
}

void BlocoDeNotas::on_actionDesfazer_triggered()
{
    ui->textEdit->undo();
}

void BlocoDeNotas::on_actionRefazer_triggered()
{
    ui->textEdit->redo();
}
