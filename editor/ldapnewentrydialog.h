#ifndef CLdapNewEntryDialog_H
#define CLdapNewEntryDialog_H

#include <QString>
#include <QVector>
#include <QDialog>
#include <CLdapData.h>

namespace Ui {
class CLdapNewEntryDialog;
}

namespace ldapeditor
{
    class CLdapNewEntryDialog : public QDialog
    {
        Q_OBJECT

    public:
        explicit CLdapNewEntryDialog(QWidget *parent, QString parentDn, ldapcore::CLdapData& ldapData);
        ~CLdapNewEntryDialog();

        QString rdn() const;
        QVector<QString> selectedClasses() const;

    private slots:
        void onCloseClicked();
        void onOkClicked();
        void onAddClicked();
        void onRemoveClicked();
        void onStructuralComboChanged(const QString&);

    private:
        Ui::CLdapNewEntryDialog* ui;
        QString          m_rdn;
        QVector<QString> vSelectedClasses;
        ldapcore::CLdapData& m_LdapData;
    };
}//namespace ldapeditor

#endif // CLdapNewEntryDialog_H