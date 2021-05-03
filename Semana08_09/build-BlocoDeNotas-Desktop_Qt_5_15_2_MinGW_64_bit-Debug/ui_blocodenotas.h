/********************************************************************************
** Form generated from reading UI file 'blocodenotas.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BLOCODENOTAS_H
#define UI_BLOCODENOTAS_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BlocoDeNotas
{
public:
    QAction *actionNovo;
    QAction *actionAbrir;
    QAction *actionSalvar;
    QAction *actionSalvar_Como;
    QAction *actionFechar;
    QAction *actionCopiar;
    QAction *actionRecortar;
    QAction *actionColar;
    QAction *actionDesfazer;
    QAction *actionRefazer;
    QAction *actionSistema_Digital;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QTextEdit *textEdit;
    QMenuBar *menubar;
    QMenu *menuArquivos;
    QMenu *menuEditar;
    QMenu *menuSobre;
    QStatusBar *statusbar;
    QToolBar *toolBar;

    void setupUi(QMainWindow *BlocoDeNotas)
    {
        if (BlocoDeNotas->objectName().isEmpty())
            BlocoDeNotas->setObjectName(QString::fromUtf8("BlocoDeNotas"));
        BlocoDeNotas->resize(800, 600);
        actionNovo = new QAction(BlocoDeNotas);
        actionNovo->setObjectName(QString::fromUtf8("actionNovo"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icones/Icones/new.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionNovo->setIcon(icon);
        actionAbrir = new QAction(BlocoDeNotas);
        actionAbrir->setObjectName(QString::fromUtf8("actionAbrir"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icones/Icones/abrir-contorno-da-pasta.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionAbrir->setIcon(icon1);
        actionSalvar = new QAction(BlocoDeNotas);
        actionSalvar->setObjectName(QString::fromUtf8("actionSalvar"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icones/Icones/salvar-silhueta-de-icone.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSalvar->setIcon(icon2);
        actionSalvar_Como = new QAction(BlocoDeNotas);
        actionSalvar_Como->setObjectName(QString::fromUtf8("actionSalvar_Como"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icones/Icones/floppy-disk.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSalvar_Como->setIcon(icon3);
        actionFechar = new QAction(BlocoDeNotas);
        actionFechar->setObjectName(QString::fromUtf8("actionFechar"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icones/Icones/botao-de-energia-desligado.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionFechar->setIcon(icon4);
        actionCopiar = new QAction(BlocoDeNotas);
        actionCopiar->setObjectName(QString::fromUtf8("actionCopiar"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icones/Icones/copiar-documento.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionCopiar->setIcon(icon5);
        actionRecortar = new QAction(BlocoDeNotas);
        actionRecortar->setObjectName(QString::fromUtf8("actionRecortar"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icones/Icones/tesouras-e-linhas-de-recorte.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionRecortar->setIcon(icon6);
        actionColar = new QAction(BlocoDeNotas);
        actionColar->setObjectName(QString::fromUtf8("actionColar"));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/icones/Icones/colar.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionColar->setIcon(icon7);
        actionDesfazer = new QAction(BlocoDeNotas);
        actionDesfazer->setObjectName(QString::fromUtf8("actionDesfazer"));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/icones/Icones/desfazer.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionDesfazer->setIcon(icon8);
        actionRefazer = new QAction(BlocoDeNotas);
        actionRefazer->setObjectName(QString::fromUtf8("actionRefazer"));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/icones/Icones/refazer.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionRefazer->setIcon(icon9);
        actionSistema_Digital = new QAction(BlocoDeNotas);
        actionSistema_Digital->setObjectName(QString::fromUtf8("actionSistema_Digital"));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/icones/Icones/balao-de-fala-de-conversa-escrita-com-a-letra-i-dentro-das-informacoes-para-a-interface.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSistema_Digital->setIcon(icon10);
        centralwidget = new QWidget(BlocoDeNotas);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        textEdit = new QTextEdit(centralwidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));

        gridLayout->addWidget(textEdit, 0, 0, 1, 1);

        BlocoDeNotas->setCentralWidget(centralwidget);
        menubar = new QMenuBar(BlocoDeNotas);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 800, 21));
        menuArquivos = new QMenu(menubar);
        menuArquivos->setObjectName(QString::fromUtf8("menuArquivos"));
        menuEditar = new QMenu(menubar);
        menuEditar->setObjectName(QString::fromUtf8("menuEditar"));
        menuSobre = new QMenu(menubar);
        menuSobre->setObjectName(QString::fromUtf8("menuSobre"));
        BlocoDeNotas->setMenuBar(menubar);
        statusbar = new QStatusBar(BlocoDeNotas);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        BlocoDeNotas->setStatusBar(statusbar);
        toolBar = new QToolBar(BlocoDeNotas);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        BlocoDeNotas->addToolBar(Qt::TopToolBarArea, toolBar);

        menubar->addAction(menuArquivos->menuAction());
        menubar->addAction(menuEditar->menuAction());
        menubar->addAction(menuSobre->menuAction());
        menuArquivos->addAction(actionNovo);
        menuArquivos->addAction(actionAbrir);
        menuArquivos->addSeparator();
        menuArquivos->addAction(actionSalvar);
        menuArquivos->addAction(actionSalvar_Como);
        menuArquivos->addSeparator();
        menuArquivos->addAction(actionFechar);
        menuEditar->addAction(actionDesfazer);
        menuEditar->addAction(actionRefazer);
        menuEditar->addSeparator();
        menuEditar->addAction(actionCopiar);
        menuEditar->addAction(actionRecortar);
        menuEditar->addAction(actionColar);
        menuSobre->addAction(actionSistema_Digital);
        toolBar->addAction(actionNovo);
        toolBar->addAction(actionAbrir);
        toolBar->addAction(actionSalvar);
        toolBar->addAction(actionSalvar_Como);
        toolBar->addSeparator();
        toolBar->addAction(actionCopiar);
        toolBar->addAction(actionRecortar);
        toolBar->addAction(actionColar);
        toolBar->addSeparator();
        toolBar->addAction(actionDesfazer);
        toolBar->addAction(actionRefazer);
        toolBar->addSeparator();
        toolBar->addAction(actionSistema_Digital);
        toolBar->addSeparator();
        toolBar->addAction(actionFechar);

        retranslateUi(BlocoDeNotas);

        QMetaObject::connectSlotsByName(BlocoDeNotas);
    } // setupUi

    void retranslateUi(QMainWindow *BlocoDeNotas)
    {
        BlocoDeNotas->setWindowTitle(QCoreApplication::translate("BlocoDeNotas", "BlocoDeNotas", nullptr));
        actionNovo->setText(QCoreApplication::translate("BlocoDeNotas", "Novo", nullptr));
        actionAbrir->setText(QCoreApplication::translate("BlocoDeNotas", "Abrir", nullptr));
        actionSalvar->setText(QCoreApplication::translate("BlocoDeNotas", "Salvar", nullptr));
        actionSalvar_Como->setText(QCoreApplication::translate("BlocoDeNotas", "Salvar Como", nullptr));
        actionFechar->setText(QCoreApplication::translate("BlocoDeNotas", "Fechar", nullptr));
        actionCopiar->setText(QCoreApplication::translate("BlocoDeNotas", "Copiar", nullptr));
        actionRecortar->setText(QCoreApplication::translate("BlocoDeNotas", "Recortar", nullptr));
        actionColar->setText(QCoreApplication::translate("BlocoDeNotas", "Colar", nullptr));
        actionDesfazer->setText(QCoreApplication::translate("BlocoDeNotas", "Desfazer", nullptr));
        actionRefazer->setText(QCoreApplication::translate("BlocoDeNotas", "Refazer", nullptr));
        actionSistema_Digital->setText(QCoreApplication::translate("BlocoDeNotas", "Sistema Digital", nullptr));
        menuArquivos->setTitle(QCoreApplication::translate("BlocoDeNotas", "Arquivos", nullptr));
        menuEditar->setTitle(QCoreApplication::translate("BlocoDeNotas", "Editar", nullptr));
        menuSobre->setTitle(QCoreApplication::translate("BlocoDeNotas", "Sobre", nullptr));
        toolBar->setWindowTitle(QCoreApplication::translate("BlocoDeNotas", "toolBar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class BlocoDeNotas: public Ui_BlocoDeNotas {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BLOCODENOTAS_H
