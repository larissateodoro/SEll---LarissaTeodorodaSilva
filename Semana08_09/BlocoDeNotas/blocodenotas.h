#ifndef BLOCODENOTAS_H
#define BLOCODENOTAS_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class BlocoDeNotas; }
QT_END_NAMESPACE

class BlocoDeNotas : public QMainWindow
{
    Q_OBJECT

public:
    BlocoDeNotas(QWidget *parent = nullptr);
    ~BlocoDeNotas();

private slots:
    void on_actionNovo_triggered();

    void on_actionAbrir_triggered();

    void on_actionSalvar_Como_triggered();

    void on_actionSalvar_triggered();

    void on_actionFechar_triggered();

    void on_actionRecortar_triggered();

    void on_actionCopiar_triggered();

    void on_actionColar_triggered();

    void on_actionDesfazer_triggered();

    void on_actionRefazer_triggered();

private:
    Ui::BlocoDeNotas *ui;
    QString local_arquivo;
};
#endif // BLOCODENOTAS_H
