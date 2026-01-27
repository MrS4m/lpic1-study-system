"""
Sistema de Estudo LPIC-1 - Tópicos 101 ao 104
Aplicativo de perguntas com interface gráfica para preparação para certificação LPIC-1

INSTALAÇÃO NO WINDOWS:
1. Instale Python 3.8+ de https://www.python.org/downloads/
2. Durante instalação, marque "Add Python to PATH"
3. Abra o Prompt de Comando e execute: pip install pillow
4. Salve este código como lpic1_app.py
5. Execute: python lpic1_app.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
from typing import List, Dict, Tuple
import json
import base64
import tempfile
import os

class QuestionBank:
    """Banco de questões LPIC-1 baseado no conteúdo oficial"""
    
    def __init__(self):
        self.questions = {
            "101.1": self._get_101_1_questions(),
            "101.2": self._get_101_2_questions(),
            "101.3": self._get_101_3_questions(),
            "102.1": self._get_102_1_questions(),
            "102.2": self._get_102_2_questions(),
            "102.3": self._get_102_3_questions(),
            "102.4": self._get_102_4_questions(),
            "102.5": self._get_102_5_questions(),
            "103.1": self._get_103_1_questions(),
            "103.2": self._get_103_2_questions(),
            "103.3": self._get_103_3_questions(),
            "103.4": self._get_103_4_questions(),
            "104.1": self._get_104_1_questions(),
            "104.2": self._get_104_2_questions(),
            "104.3": self._get_104_3_questions(),
        }
    
    def _get_101_1_questions(self):
        """101.1 Determinar e configurar hardware"""
        return [
            {
                "question": "Qual comando exibe informações sobre dispositivos PCI?",
                "type": "multiple",
                "options": ["lspci", "lsusb", "lsblk", "lscpu"],
                "correct": 0,
                "explanation": "lspci lista dispositivos PCI conectados. Opções: -v (verbose), -vv (muito verbose), -k (mostra driver kernel)."
            },
            {
                "question": "Qual comando exibe dispositivos USB?",
                "type": "multiple",
                "options": ["lsusb", "usbdev", "lspci", "hwlist"],
                "correct": 0,
                "explanation": "lsusb mostra dispositivos USB. lsusb -t mostra em formato de árvore."
            },
            {
                "question": "Onde o Linux armazena informações do sistema em tempo real?",
                "type": "multiple",
                "options": ["/proc", "/sys", "/dev", "/etc"],
                "correct": 0,
                "explanation": "/proc é filesystem virtual com informações de processos e sistema."
            },
            {
                "question": "Qual arquivo mostra informações da CPU?",
                "type": "multiple",
                "options": ["/proc/cpuinfo", "/proc/meminfo", "/proc/version", "/proc/interrupts"],
                "correct": 0,
                "explanation": "/proc/cpuinfo mostra detalhes como modelo, cores, frequência."
            },
            {
                "question": "Qual comando exibe módulos do kernel carregados?",
                "type": "multiple",
                "options": ["lsmod", "modprobe", "insmod", "rmmod"],
                "correct": 0,
                "explanation": "lsmod lista módulos do kernel atualmente carregados."
            },
            {
                "question": "Qual comando carrega módulo do kernel com dependências?",
                "type": "multiple",
                "options": ["modprobe", "insmod", "loadmod", "kmod"],
                "correct": 0,
                "explanation": "modprobe carrega módulo e suas dependências automaticamente."
            },
            {
                "question": "Qual diretório contém módulos do kernel?",
                "type": "multiple",
                "options": ["/lib/modules", "/usr/lib/modules", "/etc/modules", "/proc/modules"],
                "correct": 0,
                "explanation": "/lib/modules/$(uname -r)/ contém módulos da versão atual do kernel."
            },
            {
                "question": "Qual comando mostra informações detalhadas de hardware?",
                "type": "multiple",
                "options": ["lshw", "hwinfo", "dmidecode", "Todos os anteriores"],
                "correct": 3,
                "explanation": "lshw, hwinfo e dmidecode mostram informações detalhadas de hardware."
            },
            {
                "question": "Onde ficam arquivos de dispositivos de bloco?",
                "type": "multiple",
                "options":["/dev", "/proc", "/sys", "/media"],
                "correct": 0,
                "explanation": "/dev contém arquivos especiais que representam dispositivos."
            },
            {
                "question": "Qual comando exibe mensagens do kernel?",
                "type": "multiple",
                "options": ["dmesg", "kmsg", "syslog", "journalctl"],
                "correct": 0,
                "explanation": "dmesg exibe mensagens do buffer do kernel. dmesg -T mostra com timestamp."
            },
            {
                "question": "Qual comando mostra uso de memória?",
                "type": "multiple",
                "options": ["free", "meminfo", "vmstat", "top"],
                "correct": 0,
                "explanation": "free mostra uso de memória RAM e swap. free -h mostra em formato human-readable."
            },
            {
                "question": "Qual arquivo contém informações sobre interrupções?",
                "type": "multiple",
                "options": ["/proc/interrupts", "/proc/ioports", "/proc/dma", "/proc/irq"],
                "correct": 0,
                "explanation": "/proc/interrupts mostra IRQs em uso e estatísticas."
            },
            {
                "question": "Qual comando remove módulo do kernel?",
                "type": "multiple",
                "options": ["rmmod", "modprobe -r", "modunload", "a e b"],
                "correct": 3,
                "explanation": "rmmod remove módulo, modprobe -r remove com dependências."
            },
            {
                "question": "Onde o udev armazena regras personalizadas?",
                "type": "multiple",
                "options": ["/etc/udev/rules.d", "/usr/lib/udev/rules.d", "/lib/udev/rules.d", "a e b"],
                "correct": 3,
                "explanation": "/etc/udev/rules.d para regras personalizadas, /usr/lib/udev/rules.d para padrão do sistema."
            },
            {
                "question": "Qual comando exibe informações do loader udev?",
                "type": "multiple",
                "options": ["udevadm info", "udevinfo", "lsudev", "udevstat"],
                "correct": 0,
                "explanation": "udevadm info --query=all --name=/dev/sda mostra informações detalhadas do dispositivo."
            }
        ]
    
    def _get_101_2_questions(self):
        """101.2 Boot do sistema"""
        return [
            {
                "question": "Qual é o primeiro processo iniciado pelo kernel Linux?",
                "type": "multiple",
                "options": ["systemd/init", "bash", "login", "getty"],
                "correct": 0,
                "explanation": "systemd (ou init no SysV) é o primeiro processo (PID 1)."
            },
            {
                "question": "Qual runlevel é modo multiusuário com rede?",
                "type": "multiple",
                "options": ["3", "5", "1", "0"],
                "correct": 0,
                "explanation": "Runlevel 3: modo multiusuário com rede (texto). Runlevel 5: modo gráfico."
            },
            {
                "question": "Qual target systemd corresponde ao runlevel 5?",
                "type": "multiple",
                "options": ["graphical.target", "multi-user.target", "rescue.target", "network.target"],
                "correct": 0,
                "explanation": "graphical.target = runlevel 5, multi-user.target = runlevel 3."
            },
            {
                "question": "Qual comando altera target padrão no systemd?",
                "type": "multiple",
                "options": ["systemctl set-default", "systemctl isolate", "systemctl enable", "telinit"],
                "correct": 0,
                "explanation": "systemctl set-default graphical.target define target gráfico como padrão."
            },
            {
                "question": "Onde ficam scripts SysV init no Debian?",
                "type": "multiple",
                "options": ["/etc/init.d", "/etc/rc.d", "/etc/systemd", "/usr/lib/systemd"],
                "correct": 0,
                "explanation": "/etc/init.d contém scripts SysV no Debian/Ubuntu."
            },
            {
                "question": "Qual arquivo define runlevel padrão no SysV?",
                "type": "multiple",
                "options": ["/etc/inittab", "/etc/init/rc-sysinit.conf", "/etc/default/grub", "/boot/grub/grub.cfg"],
                "correct": 0,
                "explanation": "/etc/inittab define runlevel padrão em sistemas SysV."
            },
            {
                "question": "Qual comando recarrega daemon systemd?",
                "type": "multiple",
                "options": ["systemctl daemon-reload", "systemctl reload", "systemctl restart", "init q"],
                "correct": 0,
                "explanation": "systemctl daemon-reload recarrega arquivos de unit após modificação."
            },
            {
                "question": "Qual tecla edita entrada GRUB durante boot?",
                "type": "multiple",
                "options": ["e", "c", "Esc", "F2"],
                "correct": 0,
                "explanation": "Tecla 'e' no GRUB permite editar parâmetros de boot temporariamente."
            },
            {
                "question": "Qual arquivo configura GRUB2?",
                "type": "multiple",
                "options": ["/etc/default/grub", "/boot/grub/grub.cfg", "/etc/grub.d", "a e c"],
                "correct": 3,
                "explanation": "/etc/default/grub para opções principais, /etc/grub.d/ para scripts."
            },
            {
                "question": "Qual comando atualiza GRUB2 no Ubuntu?",
                "type": "multiple",
                "options": ["update-grub", "grub-mkconfig", "grub2-mkconfig", "a e b"],
                "correct": 3,
                "explanation": "update-grub é alias para grub-mkconfig -o /boot/grub/grub.cfg"
            },
            {
                "question": "Qual parâmetro do kernel boota em modo single-user?",
                "type": "multiple",
                "options": ["single", "1", "s", "Todos anteriores"],
                "correct": 3,
                "explanation": "single, 1 ou s iniciam modo single-user (rescue)."
            },
            {
                "question": "Qual comando mostra serviços systemd habilitados?",
                "type": "multiple",
                "options": ["systemctl list-unit-files --state=enabled", "systemctl list-units --type=service", "service --status-all", "chkconfig --list"],
                "correct": 0,
                "explanation": "systemctl list-unit-files --state=enabled lista unidades habilitadas."
            },
            {
                "question": "Onde systemd armazena unit files do sistema?",
                "type": "multiple",
                "options": ["/usr/lib/systemd/system", "/etc/systemd/system", "/lib/systemd/system", "a e b"],
                "correct": 3,
                "explanation": "/usr/lib/systemd/system para unidades padrão, /etc/systemd/system para customizadas."
            },
            {
                "question": "Qual comando mostra logs do systemd?",
                "type": "multiple",
                "options": ["journalctl", "systemctl log", "dmesg", "tail -f /var/log/syslog"],
                "correct": 0,
                "explanation": "journalctl exibe logs do systemd. journalctl -f segue logs em tempo real."
            },
            {
                "question": "Qual target é modo de emergência?",
                "type": "multiple",
                "options": ["emergency.target", "rescue.target", "multi-user.target", "graphical.target"],
                "correct": 0,
                "explanation": "emergency.target é modo mais mínimo que rescue.target."
            }
        ]
    
    def _get_101_3_questions(self):
        """101.3 Alterar runlevels e shutdown/reboot"""
        return [
            {
                "question": "Qual comando desliga sistema imediatamente?",
                "type": "multiple",
                "options": ["shutdown -h now", "poweroff", "halt", "Todos anteriores"],
                "correct": 3,
                "explanation": "Todos desligam o sistema. shutdown oferece mais opções como agendamento."
            },
            {
                "question": "Qual comando reinicia sistema em 5 minutos?",
                "type": "multiple",
                "options": ["shutdown -r +5", "reboot +5", "restart 5", "init 6 +5"],
                "correct": 0,
                "explanation": "shutdown -r +5 agenda reboot para 5 minutos."
            },
            {
                "question": "Como cancelar shutdown agendado?",
                "type": "multiple",
                "options": ["shutdown -c", "shutdown --cancel", "cancel shutdown", "init 0 cancel"],
                "correct": 0,
                "explanation": "shutdown -c cancela shutdown/reboot agendado."
            },
            {
                "question": "Qual comando muda runlevel no SysV?",
                "type": "multiple",
                "options": ["init", "telinit", "runlevel", "a e b"],
                "correct": 3,
                "explanation": "init e telinit mudam runlevel (ex: init 3)."
            },
            {
                "question": "Qual comando mostra runlevel atual?",
                "type": "multiple",
                "options": ["runlevel", "who -r", "systemctl get-default", "a e b"],
                "correct": 3,
                "explanation": "runlevel mostra anterior e atual. who -r também mostra."
            },
            {
                "question": "Qual sinal é enviado primeiro durante shutdown?",
                "type": "multiple",
                "options": ["SIGTERM", "SIGKILL", "SIGHUP", "SIGINT"],
                "correct": 0,
                "explanation": "SIGTERM permite término gracioso. SIGKILL é forçado se processo não terminar."
            },
            {
                "question": "Qual comando systemd suspende sistema?",
                "type": "multiple",
                "options": ["systemctl suspend", "systemctl hibernate", "systemctl hybrid-sleep", "pm-suspend"],
                "correct": 0,
                "explanation": "systemctl suspend coloca em suspensão (sleep)."
            },
            {
                "question": "Qual comando hiberna sistema?",
                "type": "multiple",
                "options": ["systemctl hibernate", "suspend-to-disk", "hibernate", "pm-hibernate"],
                "correct": 0,
                "explanation": "systemctl hibernate salva estado em disco e desliga."
            },
            {
                "question": "Qual runlevel desliga sistema?",
                "type": "multiple",
                "options": ["0", "6", "1", "5"],
                "correct": 0,
                "explanation": "Runlevel 0: halt, Runlevel 6: reboot."
            },
            {
                "question": "Qual comando envia mensagem a todos usuários?",
                "type": "multiple",
                "options": ["wall", "broadcast", "message", "shout"],
                "correct": 0,
                "explanation": "wall 'mensagem' envia broadcast para todos usuários logados."
            },
            {
                "question": "Qual comando mostra tempo de atividade do sistema?",
                "type": "multiple",
                "options": ["uptime", "w", "who -b", "a e b"],
                "correct": 3,
                "explanation": "uptime mostra tempo ligado e carga. w também mostra."
            },
            {
                "question": "Qual arquivo impede novos logins durante shutdown?",
                "type": "multiple",
                "options": ["/run/nologin", "/etc/nologin", "/var/run/nologin", "a e c"],
                "correct": 3,
                "explanation": "/run/nologin ou /etc/nologin impedem novos logins durante shutdown."
            },
            {
                "question": "Qual comando força fsck no próximo boot?",
                "type": "multiple",
                "options": ["touch /forcefsck", "shutdown -F", "fsck -f", "a e b"],
                "correct": 3,
                "explanation": "touch /forcefsck ou shutdown -F forçam verificação de disco no boot."
            },
            {
                "question": "Como analisar tempo de boot no systemd?",
                "type": "multiple",
                "options": ["systemd-analyze", "systemd-analyze blame", "systemd-analyze critical-chain", "Todos anteriores"],
                "correct": 3,
                "explanation": "systemd-analyze mostra tempo total, blame por serviço, critical-chain cadeia crítica."
            },
            {
                "question": "Qual comando mostra unidades systemd que falharam?",
                "type": "multiple",
                "options": ["systemctl --failed", "systemctl list-units --state=failed", "journalctl -p err", "a e b"],
                "correct": 3,
                "explanation": "systemctl --failed lista unidades com falha."
            }
        ]
    
    def _get_102_1_questions(self):
        """102.1 Design layout de disco"""
        return [
            {
                "question": "Qual diretório DEVE estar em partição separada?",
                "type": "multiple",
                "options": ["/home", "/bin", "/lib", "/etc"],
                "correct": 0,
                "explanation": "/home deve estar separado para facilitar backup, reinstalação e quotas."
            },
            {
                "question": "Qual diretório contém logs variáveis?",
                "type": "multiple",
                "options": ["/var", "/tmp", "/opt", "/usr"],
                "correct": 0,
                "explanation": "/var contém logs, spools, caches que crescem com o tempo."
            },
            {
                "question": "Qual tabela de partição suporta discos >2TB?",
                "type": "multiple",
                "options": ["GPT", "MBR", "DOS", "BIOS"],
                "correct": 0,
                "explanation": "GPT (GUID Partition Table) suporta discos até 9.4ZB. MBR limita a 2TB."
            },
            {
                "question": "Quantas partições primárias MBR suporta?",
                "type": "multiple",
                "options": ["4", "16", "128", "ilimitadas"],
                "correct": 0,
                "explanation": "MBR: 4 primárias, ou 3 primárias + 1 estendida com lógicas."
            },
            {
                "question": "Qual tamanho mínimo recomendado para /boot?",
                "type": "multiple",
                "options": ["500MB", "100MB", "1GB", "2GB"],
                "correct": 0,
                "explanation": "500MB permite múltiplos kernels e initramfs."
            },
            {
                "question": "Qual partição é obrigatória em sistemas UEFI?",
                "type": "multiple",
                "options": ["EFI System Partition (ESP)", "/boot", "BIOS boot", "swap"],
                "correct": 0,
                "explanation": "ESP (FAT32) contém bootloaders UEFI. Normalmente montada em /boot/efi."
            },
            {
                "question": "Qual sistema de arquivos para ESP?",
                "type": "multiple",
                "options": ["FAT32", "ext4", "XFS", "Btrfs"],
                "correct": 0,
                "explanation": "ESP deve ser FAT32 para compatibilidade UEFI."
            },
            {
                "question": "Qual comando lista partições?",
                "type": "multiple",
                "options": ["lsblk", "fdisk -l", "parted -l", "Todos anteriores"],
                "correct": 3,
                "explanation": "lsblk formato árvore, fdisk -l e parted -l listam partições."
            },
            {
                "question": "Qual código fdisk para partição Linux?",
                "type": "multiple",
                "options": ["83", "82", "8e", "fd"],
                "correct": 0,
                "explanation": "83: Linux filesystem, 82: Linux swap, 8e: Linux LVM, fd: Linux RAID."
            },
            {
                "question": "Qual comando mostra uso de espaço em disco?",
                "type": "multiple",
                "options": ["df", "du", "lsblk", "fdisk"],
                "correct": 0,
                "explanation": "df mostra uso por filesystem. df -h em formato human-readable."
            },
            {
                "question": "Qual diretório para dados de servidor web?",
                "type": "multiple",
                "options": ["/srv", "/var/www", "/home/www", "a e b"],
                "correct": 3,
                "explanation": "/srv ou /var/www são comuns para conteúdo web."
            },
            {
                "question": "Qual tamanho swap para 8GB RAM?",
                "type": "multiple",
                "options": ["8GB", "4GB", "16GB", "depende do uso"],
                "correct": 3,
                "explanation": "Swap depende: desktop 2GB suficiente, servidor precisa mais, hibernação precisa igual à RAM."
            },
            {
                "question": "Qual comando cria partições GPT?",
                "type": "multiple",
                "options": ["gdisk", "parted", "fdisk (versões recentes)", "Todos anteriores"],
                "correct": 3,
                "explanation": "gdisk especializado em GPT, parted também, fdisk moderno suporta."
            },
            {
                "question": "Onde montar sistema de arquivos temporário em RAM?",
                "type": "multiple",
                "options": ["/tmp", "/var/tmp", "/dev/shm", "a e c"],
                "correct": 3,
                "explanation": "/tmp pode ser tmpfs. /dev/shm é shared memory POSIX."
            },
            {
                "question": "Qual diretório NÃO deve estar em partição separada?",
                "type": "multiple",
                "options": ["/bin", "/home", "/var", "/opt"],
                "correct": 0,
                "explanation": "/bin, /sbin, /lib são críticos para boot e devem estar na raiz."
            }
        ]
    
    def _get_102_2_questions(self):
        """102.2 Instalar gerenciador de boot"""
        return [
            {
                "question": "Qual comando instala GRUB2 no MBR?",
                "type": "multiple",
                "options": ["grub-install /dev/sda", "grub-setup /dev/sda", "install-grub", "update-grub"],
                "correct": 0,
                "explanation": "grub-install /dev/sda instala no MBR. NÃO use /dev/sda1 (partição)."
            },
            {
                "question": "Qual arquivo de configuração GRUB2 principal?",
                "type": "multiple",
                "options": ["/boot/grub/grub.cfg", "/etc/default/grub", "/etc/grub.d", "/boot/grub/menu.lst"],
                "correct": 0,
                "explanation": "grub.cfg é gerado automaticamente. Não edite manualmente."
            },
            {
                "question": "Onde configurar opções GRUB2?",
                "type": "multiple",
                "options": ["/etc/default/grub", "/boot/grub/grub.cfg", "/etc/grub.conf", "/boot/grub/menu.lst"],
                "correct": 0,
                "explanation": "/etc/default/grub contém variáveis como GRUB_TIMEOUT, GRUB_CMDLINE_LINUX."
            },
            {
                "question": "Qual comando gera grub.cfg?",
                "type": "multiple",
                "options": ["grub-mkconfig -o /boot/grub/grub.cfg", "update-grub", "grub2-mkconfig", "Todos anteriores"],
                "correct": 3,
                "explanation": "update-grub é alias para grub-mkconfig. No RHEL: grub2-mkconfig."
            },
            {
                "question": "Qual variável define timeout do menu GRUB?",
                "type": "multiple",
                "options": ["GRUB_TIMEOUT", "GRUB_DEFAULT", "GRUB_CMDLINE_LINUX", "GRUB_HIDDEN_TIMEOUT"],
                "correct": 0,
                "explanation": "GRUB_TIMEOUT=5 espera 5 segundos. 0 não mostra menu."
            },
            {
                "question": "Como instalar GRUB2 em UEFI?",
                "type": "multiple",
                "options": ["grub-install --target=x86_64-efi --efi-directory=/boot/efi", "grub-install /dev/sda", "grub2-install", "install-grub-uefi"],
                "correct": 0,
                "explanation": "Em UEFI, especificar --target e --efi-directory para ESP."
            },
            {
                "question": "Qual comando lista entradas de boot UEFI?",
                "type": "multiple",
                "options": ["efibootmgr", "uefivars", "bootlist", "grub-probe"],
                "correct": 0,
                "explanation": "efibootmgr -v mostra entradas UEFI. efibootmgr -c cria nova."
            },
            {
                "question": "Onde GRUB2 armazena módulos?",
                "type": "multiple",
                "options": ["/boot/grub", "/usr/lib/grub", "/lib/grub", "/etc/grub.d"],
                "correct": 0,
                "explanation": "/boot/grub/ contém módulos (*.mod) e arquivos de configuração."
            },
            {
                "question": "Qual arquivo detecta outros sistemas operacionais?",
                "type": "multiple",
                "options": ["/etc/grub.d/30_os-prober", "/etc/default/grub", "/boot/grub/grub.cfg", "/usr/lib/os-prober"],
                "correct": 0,
                "explanation": "30_os-prober detecta Windows, Linux, etc. para dual-boot."
            },
            {
                "question": "Como referenciar primeira partição do segundo disco no GRUB?",
                "type": "multiple",
                "options": ["(hd1,1)", "(sdb1)", "(hd1,msdos1)", "a e c"],
                "correct": 3,
                "explanation": "GRUB usa (hdN,M) onde N=disco (0-index), M=partição (1-index). msdos para MBR."
            },
            {
                "question": "Qual tecla abre linha de comando GRUB?",
                "type": "multiple",
                "options": ["c", "e", "Esc", "F2"],
                "correct": 0,
                "explanation": "'c' abre shell GRUB para comandos manuais."
            },
            {
                "question": "Qual arquivo GRUB Legacy (antigo)?",
                "type": "multiple",
                "options": ["/boot/grub/menu.lst", "/etc/grub.conf", "/boot/grub/grub.cfg", "a e b"],
                "correct": 3,
                "explanation": "GRUB Legacy: menu.lst (Debian) ou grub.conf (RHEL)."
            },
            {
                "question": "Como desabilitar submenu de kernels antigos?",
                "type": "multiple",
                "options": ["GRUB_DISABLE_SUBMENU=true", "GRUB_HIDDEN_TIMEOUT=0", "GRUB_TIMEOUT_STYLE=hidden", "GRUB_DEFAULT=saved"],
                "correct": 0,
                "explanation": "GRUB_DISABLE_SUBMENU=y mostra todos kernels no menu principal."
            },
            {
                "question": "Qual variável define parâmetros do kernel?",
                "type": "multiple",
                "options": ["GRUB_CMDLINE_LINUX", "GRUB_KERNEL_OPTS", "GRUB_BOOT_ARGS", "GRUB_LINUX_CMDLINE"],
                "correct": 0,
                "explanation": "GRUB_CMDLINE_LINUX='quiet splash' define parâmetros passados ao kernel."
            },
            {
                "question": "Como recuperar GRUB após instalação Windows?",
                "type": "multiple",
                "options": ["Boot com Live CD, chroot, grub-install", "Reparar com bootrec no Windows", "Usar Super GRUB Disk", "a e c"],
                "correct": 3,
                "explanation": "Windows sobrescreve MBR. Use Live Linux para reinstalar GRUB."
            }
        ]
    
    def _get_102_3_questions(self):
        """102.3 Gerenciar bibliotecas compartilhadas"""
        return [
            {
                "question": "Qual comando mostra dependências de bibliotecas?",
                "type": "multiple",
                "options": ["ldd", "ldconfig", "objdump", "readelf"],
                "correct": 0,
                "explanation": "ldd /bin/bash mostra bibliotecas compartilhadas necessárias."
            },
            {
                "question": "Qual comando atualiza cache de bibliotecas?",
                "type": "multiple",
                "options": ["ldconfig", "ldd", "libupdate", "refresh-libs"],
                "correct": 0,
                "explanation": "ldconfig atualiza /etc/ld.so.cache com bibliotecas encontradas."
            },
            {
                "question": "Onde configurar diretórios de bibliotecas?",
                "type": "multiple",
                "options": ["/etc/ld.so.conf", "/etc/ld.so.conf.d/*.conf", "/etc/ld.so.cache", "a e b"],
                "correct": 3,
                "explanation": "/etc/ld.so.conf e arquivos .conf em ld.so.conf.d/ definem diretórios de busca."
            },
            {
                "question": "Qual variável adiciona diretórios à busca de bibliotecas?",
                "type": "multiple",
                "options": ["LD_LIBRARY_PATH", "LIBRARY_PATH", "LD_PATH", "LIB_PATH"],
                "correct": 0,
                "explanation": "LD_LIBRARY_PATH=/caminho/extra adiciona diretórios à busca em tempo de execução."
            },
            {
                "question": "Qual prefixo de bibliotecas compartilhadas Linux?",
                "type": "multiple",
                "options": ["lib", "so", "dll", "dylib"],
                "correct": 0,
                "explanation": "libnome.so.versão (ex: libc.so.6). .so = Shared Object."
            },
            {
                "question": "Qual diretório para bibliotecas 64-bit?",
                "type": "multiple",
                "options": ["/lib64", "/usr/lib64", "/lib/x86_64-linux-gnu", "Todos anteriores"],
                "correct": 3,
                "explanation": "Distribuições usam diferentes convenções: RHEL /lib64, Debian /lib/x86_64-linux-gnu."
            },
            {
                "question": "Como ver bibliotecas no cache?",
                "type": "multiple",
                "options": ["ldconfig -p", "ldconfig -v", "cat /etc/ld.so.cache", "ls /lib"],
                "correct": 0,
                "explanation": "ldconfig -p mostra bibliotecas conhecidas pelo cache."
            },
            {
                "question": "Qual variável força carregamento de biblioteca?",
                "type": "multiple",
                "options": ["LD_PRELOAD", "LD_LOAD", "PRELOAD_LIB", "LIB_PRELOAD"],
                "correct": 0,
                "explanation": "LD_PRELOAD=/caminho/lib.so força carregamento antes das outras."
            },
            {
                "question": "Qual comando mostra informações ELF?",
                "type": "multiple",
                "options": ["readelf", "file", "objdump", "Todos anteriores"],
                "correct": 3,
                "explanation": "readelf -h mostra cabeçalho ELF, file identifica tipo, objdump desmonta."
            },
            {
                "question": "Qual loader para binários 64-bit?",
                "type": "multiple",
                "options": ["/lib64/ld-linux-x86-64.so.2", "/lib/ld-linux.so.2", "/usr/lib/ld.so", "/bin/ld"],
                "correct": 0,
                "explanation": "64-bit: /lib64/ld-linux-x86-64.so.2, 32-bit: /lib/ld-linux.so.2"
            },
            {
                "question": "Onde instalar bibliotecas locais?",
                "type": "multiple",
                "options": ["/usr/local/lib", "/opt/lib", "/home/user/lib", "a e b"],
                "correct": 3,
                "explanation": "/usr/local/lib para software compilado localmente, /opt/lib para pacotes em /opt."
            },
            {
                "question": "Como ver versão de biblioteca?",
                "type": "multiple",
                "options": ["strings libc.so.6 | grep GLIBC", "objdump -p libc.so.6", "readelf -a libc.so.6", "Todos anteriores"],
                "correct": 3,
                "explanation": "Várias formas de extrair informações de versão de bibliotecas."
            },
            {
                "question": "Qual arquivo lista bibliotecas para todos processos?",
                "type": "multiple",
                "options": ["/etc/ld.so.preload", "/etc/ld.so.conf", "/etc/ld.so.cache", "/etc/preload.conf"],
                "correct": 0,
                "explanation": "/etc/ld.so.preload força bibliotecas para todos processos (cuidado!)."
            },
            {
                "question": "Como resolver 'library not found'?",
                "type": "multiple",
                "options": ["Executar ldconfig", "Verificar LD_LIBRARY_PATH", "Instalar pacote com biblioteca", "Todos anteriores"],
                "correct": 3,
                "explanation": "Primeiro ldconfig, depois verificar variáveis, finalmente instalar bibliotecas faltantes."
            },
            {
                "question": "Qual extensão para links a bibliotecas?",
                "type": "multiple",
                "options": [".so", ".so.X", ".so.X.Y.Z", "a e c"],
                "correct": 3,
                "explanation": "libfoo.so → libfoo.so.1 → libfoo.so.1.2.3 (real). ldconfig cria links."
            }
        ]
    
    def _get_102_4_questions(self):
        """102.4 Gerenciar pacotes Debian"""
        return [
            {
                "question": "Qual comando instala pacote .deb local?",
                "type": "multiple",
                "options": ["dpkg -i", "apt install", "apt-get install", "install-deb"],
                "correct": 0,
                "explanation": "dpkg -i pacote.deb instala arquivo local sem resolver dependências."
            },
            {
                "question": "Qual comando atualiza lista de pacotes?",
                "type": "multiple",
                "options": ["apt update", "apt-get update", "aptitude update", "Todos anteriores"],
                "correct": 3,
                "explanation": "Todos atualizam lista de pacotes disponíveis dos repositórios."
            },
            {
                "question": "Qual comando atualiza sistema?",
                "type": "multiple",
                "options": ["apt upgrade", "apt-get upgrade", "apt full-upgrade", "Todos anteriores"],
                "correct": 3,
                "explanation": "upgrade atualiza, full-upgrade/ dist-upgrade também lida com remoções."
            },
            {
                "question": "Como remover pacote mantendo configurações?",
                "type": "multiple",
                "options": ["apt remove", "dpkg -r", "apt-get remove", "Todos anteriores"],
                "correct": 3,
                "explanation": "remove mantém arquivos de configuração. purge remove tudo."
            },
            {
                "question": "Como remover pacote e configurações?",
                "type": "multiple",
                "options": ["apt purge", "dpkg -P", "apt-get purge", "Todos anteriores"],
                "correct": 3,
                "explanation": "purge remove pacote e arquivos de configuração."
            },
            {
                "question": "Onde configurar repositórios APT?",
                "type": "multiple",
                "options": ["/etc/apt/sources.list", "/etc/apt/sources.list.d/*.list", "/etc/apt.conf.d/", "a e b"],
                "correct": 3,
                "explanation": "sources.list principal, sources.list.d/ para arquivos adicionais."
            },
            {
                "question": "Qual comando busca pacote?",
                "type": "multiple",
                "options": ["apt search", "apt-cache search", "aptitude search", "Todos anteriores"],
                "correct": 3,
                "explanation": "search busca por nome e descrição nos repositórios."
            },
            {
                "question": "Como mostrar informações de pacote?",
                "type": "multiple",
                "options": ["apt show", "dpkg -s", "apt-cache show", "Todos anteriores"],
                "correct": 3,
                "explanation": "show info do repositório, -s info do instalado."
            },
            {
                "question": "Como listar arquivos de pacote instalado?",
                "type": "multiple",
                "options": ["dpkg -L", "dpkg --listfiles", "apt-file list", "a e b"],
                "correct": 3,
                "explanation": "dpkg -L pacote lista arquivos instalados por pacote."
            },
            {
                "question": "Como descobrir pacote dono de arquivo?",
                "type": "multiple",
                "options": ["dpkg -S", "apt-file search", "whichpkg", "a e b"],
                "correct": 3,
                "explanation": "dpkg -S /bin/ls mostra qual pacote instalou o arquivo."
            },
            {
                "question": "Onde APT armazena pacotes baixados?",
                "type": "multiple",
                "options": ["/var/cache/apt/archives", "/tmp/apt", "/var/lib/apt", "/usr/cache/apt"],
                "correct": 0,
                "explanation": "/var/cache/apt/archives/ contém arquivos .deb baixados."
            },
            {
                "question": "Como limpar cache APT?",
                "type": "multiple",
                "options": ["apt clean", "apt autoclean", "apt-get clean", "Todos anteriores"],
                "correct": 3,
                "explanation": "clean remove todos .deb, autoclean remove apenas obsoletos."
            },
            {
                "question": "Como remover pacotes órfãos?",
                "type": "multiple",
                "options": ["apt autoremove", "apt-get autoremove", "deborphan", "a e b"],
                "correct": 3,
                "explanation": "autoremove remove dependências não mais necessárias."
            },
            {
                "question": "Como listar pacotes instalados?",
                "type": "multiple",
                "options": ["dpkg -l", "apt list --installed", "aptitude search '~i'", "Todos anteriores"],
                "correct": 3,
                "explanation": "dpkg -l, apt list --installed, aptitude mostram pacotes instalados."
            },
            {
                "question": "Como reconfigurar pacote?",
                "type": "multiple",
                "options": ["dpkg-reconfigure", "apt-config", "reconfigure", "setup-package"],
                "correct": 0,
                "explanation": "dpkg-reconfigure pacote executa scripts de configuração novamente."
            }
        ]
    
    def _get_102_5_questions(self):
        """102.5 Gerenciar pacotes RPM e YUM"""
        return [
            {
                "question": "Qual comando instala pacote RPM local?",
                "type": "multiple",
                "options": ["rpm -i", "rpm -U", "yum install", "dnf install"],
                "correct": 0,
                "explanation": "rpm -ivh pacote.rpm instala localmente. -v verbose, -h hash marks."
            },
            {
                "question": "Qual comando YUM instala pacote?",
                "type": "multiple",
                "options": ["yum install", "dnf install", "zypper install", "a e b"],
                "correct": 3,
                "explanation": "yum (RHEL7), dnf (RHEL8+, Fedora), zypper (OpenSUSE)."
            },
            {
                "question": "Qual comando atualiza todos pacotes?",
                "type": "multiple",
                "options": ["yum update", "dnf upgrade", "rpm -U", "a e b"],
                "correct": 3,
                "explanation": "yum/dnf update/upgrade atualizam todos pacotes."
            },
            {
                "question": "Qual comando remove pacote com YUM?",
                "type": "multiple",
                "options": ["yum remove", "yum erase", "rpm -e", "a e b"],
                "correct": 3,
                "explanation": "yum remove pacote remove pacote e dependências não utilizadas."
            },
            {
                "question": "Como listar todos pacotes instalados?",
                "type": "multiple",
                "options": ["rpm -qa", "yum list installed", "dnf list installed", "Todos anteriores"],
                "correct": 3,
                "explanation": "rpm -qa, yum list installed, dnf list installed."
            },
            {
                "question": "Onde configurar repositórios YUM?",
                "type": "multiple",
                "options": ["/etc/yum.repos.d/*.repo", "/etc/yum.conf", "/etc/dnf/dnf.conf", "a e b"],
                "correct": 3,
                "explanation": "*.repo em yum.repos.d/ definem repositórios, yum.conf configurações gerais."
            },
            {
                "question": "Qual comando busca pacote?",
                "type": "multiple",
                "options": ["yum search", "dnf search", "rpm -q", "a e b"],
                "correct": 3,
                "explanation": "yum/dnf search busca por nome e descrição."
            },
            {
                "question": "Como mostrar informações de pacote RPM?",
                "type": "multiple",
                "options": ["rpm -qi", "yum info", "dnf info", "Todos anteriores"],
                "correct": 3,
                "explanation": "rpm -qi para instalados, yum/dnf info também de repositórios."
            },
            {
                "question": "Como listar arquivos de pacote RPM?",
                "type": "multiple",
                "options": ["rpm -ql", "rpm -q --files", "yum provides", "a e b"],
                "correct": 3,
                "explanation": "rpm -ql pacote lista arquivos instalados por pacote."
            },
            {
                "question": "Como descobrir pacote dono de arquivo?",
                "type": "multiple",
                "options": ["rpm -qf", "yum provides", "dnf provides", "Todos anteriores"],
                "correct": 3,
                "explanation": "rpm -qf /bin/ls mostra pacote que fornece o arquivo."
            },
            {
                "question": "Qual gerenciador OpenSUSE?",
                "type": "multiple",
                "options": ["zypper", "yast", "rug", "a e b"],
                "correct": 3,
                "explanation": "zypper linha de comando, YaST interface gráfica."
            },
            {
                "question": "Qual comando zypper atualiza repositórios?",
                "type": "multiple",
                "options": ["zypper refresh", "zypper update", "zypper patch", "zypper dist-upgrade"],
                "correct": 0,
                "explanation": "zypper refresh atualiza metadados dos repositórios."
            },
            {
                "question": "Como forçar instalação RPM ignorando dependências?",
                "type": "multiple",
                "options": ["rpm -i --nodeps", "rpm -i --force", "yum install --skip-broken", "rpm -i --ignoreos"],
                "correct": 0,
                "explanation": "--nodeps ignora verificações de dependência (perigoso!)."
            },
            {
                "question": "Como atualizar pacote RPM?",
                "type": "multiple",
                "options": ["rpm -U", "rpm -F", "yum update", "a e c"],
                "correct": 3,
                "explanation": "rpm -U atualiza se existir ou instala. -F apenas atualiza se existir."
            },
            {
                "question": "Como limpar cache YUM?",
                "type": "multiple",
                "options": ["yum clean all", "dnf clean all", "yum makecache", "a e b"],
                "correct": 3,
                "explanation": "yum/dnf clean all limpa todo cache. makecache recria."
            }
        ]
    
    def _get_103_1_questions(self):
        """103.1 Trabalhar na linha de comando"""
        return [
            {
                "question": "Qual variável contém PATH de comandos?",
                "type": "multiple",
                "options": ["PATH", "HOME", "SHELL", "USER"],
                "correct": 0,
                "explanation": "PATH=/bin:/usr/bin:/usr/local/bin define onde shell busca executáveis."
            },
            {
                "question": "Como definir variável de ambiente?",
                "type": "multiple",
                "options": ["export VAR=valor", "set VAR=valor", "VAR=valor", "env VAR=valor"],
                "correct": 0,
                "explanation": "export torna variável disponível para processos filhos."
            },
            {
                "question": "Como ver valor de variável?",
                "type": "multiple",
                "options": ["echo $VAR", "printenv VAR", "env | grep VAR", "Todos anteriores"],
                "correct": 3,
                "explanation": "echo $VAR, printenv VAR, env mostra todas."
            },
            {
                "question": "Qual arquivo carrega variáveis para todos usuários?",
                "type": "multiple",
                "options": ["/etc/profile", "/etc/bash.bashrc", "/etc/environment", "a e c"],
                "correct": 3,
                "explanation": "/etc/profile (bash) e /etc/environment (PAM) são carregados no login."
            },
            {
                "question": "Qual arquivo bash pessoal para login?",
                "type": "multiple",
                "options": ["~/.bash_profile", "~/.profile", "~/.bashrc", "a e b"],
                "correct": 3,
                "explanation": ".bash_profile ou .profile para login shells, .bashrc para shells interativos."
            },
            {
                "question": "Qual comando executa script no shell atual?",
                "type": "multiple",
                "options": ["source", ".", "exec", "a e b"],
                "correct": 3,
                "explanation": "source script.sh ou . script.sh executa no contexto atual (sem sub-shell)."
            },
            {
                "question": "Qual variável contém diretório home?",
                "type": "multiple",
                "options": ["HOME", "USERPROFILE", "HOMEDIR", "USERHOME"],
                "correct": 0,
                "explanation": "$HOME aponta para /home/usuario. cd ~ ou cd $HOME vão para home."
            },
            {
                "question": "Como criar alias?",
                "type": "multiple",
                "options": ["alias ll='ls -la'", "set alias ll='ls -la'", "export alias ll", "newalias ll"],
                "correct": 0,
                "explanation": "alias nome='comando' cria atalho. alias sem argumentos lista todos."
            },
            {
                "question": "Como remover alias?",
                "type": "multiple",
                "options": ["unalias ll", "alias ll=", "unset alias ll", "removealias ll"],
                "correct": 0,
                "explanation": "unalias nome remove alias específico, unalias -a remove todos."
            },
            {
                "question": "Qual comando mostra tipo de comando?",
                "type": "multiple",
                "options": ["type", "which", "whereis", "Todos anteriores"],
                "correct": 3,
                "explanation": "type mostra se é builtin, alias ou executável; which mostra caminho; whereis mostra binário, source e man."
            },
            {
                "question": "Qual símbolo executa comando em background?",
                "type": "multiple",
                "options": ["&", "&&", "|", ";"],
                "correct": 0,
                "explanation": "comando & executa em background. comando && executa se anterior sucedeu."
            },
            {
                "question": "Qual comando lista jobs?",
                "type": "multiple",
                "options": ["jobs", "ps", "bg", "fg"],
                "correct": 0,
                "explanation": "jobs lista jobs do shell atual. jobs -l mostra PIDs também."
            },
            {
                "question": "Como trazer job para foreground?",
                "type": "multiple",
                "options": ["fg", "bg", "jobs -f", "foreground"],
                "correct": 0,
                "explanation": "fg %1 traz job 1 para foreground. fg sem número traz job mais recente."
            },
            {
                "question": "Como pausar processo em foreground?",
                "type": "multiple",
                "options": ["Ctrl+Z", "Ctrl+C", "Ctrl+D", "Ctrl+barra"],
                "correct": 0,
                "explanation": "Ctrl+Z envia SIGTSTP, pausando processo. Ctrl+C envia SIGINT, terminando."
            },
            {
                "question": "Qual variável contém exit status do último comando?",
                "type": "multiple",
                "options": ["$?", "$!", "$#", "$$"],
                "correct": 0,
                "explanation": "$? contém 0 para sucesso, não-zero para erro. echo $? mostra resultado."
            }
        ]
    
    def _get_103_2_questions(self):
        """103.2 Processar streams de texto usando filtros"""
        return [
            {
                "question": "Qual comando exibe conteúdo de arquivo?",
                "type": "multiple",
                "options": ["cat", "more", "less", "Todos anteriores"],
                "correct": 3,
                "explanation": "cat concatena, more/less paginam. less é mais avançado (permite voltar)."
            },
            {
                "question": "Qual comando mostra primeiras linhas?",
                "type": "multiple",
                "options": ["head", "top", "first", "header"],
                "correct": 0,
                "explanation": "head -n 20 arquivo mostra primeiras 20 linhas. Padrão: 10 linhas."
            },
            {
                "question": "Qual comando mostra últimas linhas?",
                "type": "multiple",
                "options": ["tail", "end", "last", "bottom"],
                "correct": 0,
                "explanation": "tail -n 20 arquivo mostra últimas 20 linhas. tail -f segue em tempo real."
            },
            {
                "question": "Qual comando conta linhas, palavras, caracteres?",
                "type": "multiple",
                "options": ["wc", "count", "lc", "stats"],
                "correct": 0,
                "explanation": "wc -l conta linhas, -w palavras, -c bytes, -m caracteres."
            },
            {
                "question": "Qual comando ordena linhas?",
                "type": "multiple",
                "options": ["sort", "order", "arrange", "rank"],
                "correct": 0,
                "explanation": "sort ordena alfabeticamente. sort -n numericamente, -r reverso, -u único."
            },
            {
                "question": "Qual comando remove linhas duplicadas consecutivas?",
                "type": "multiple",
                "options": ["uniq", "unique", "dedup", "rmdups"],
                "correct": 0,
                "explanation": "uniq remove duplicatas consecutivas. Geralmente usado com sort: sort | uniq."
            },
            {
                "question": "Qual comando extrai colunas?",
                "type": "multiple",
                "options": ["cut", "awk", "col", "a e b"],
                "correct": 3,
                "explanation": "cut -d: -f1 extrai primeiro campo delimitado por ':'. awk é mais poderoso."
            },
            {
                "question": "Qual comando traduz/deleta caracteres?",
                "type": "multiple",
                "options": ["tr", "translate", "char", "sed 'y/'"],
                "correct": 0,
                "explanation": "tr 'a-z' 'A-Z' converte minúsculas para maiúsculas. tr -d '0-9' remove dígitos."
            },
            {
                "question": "Qual comando busca padrões em texto?",
                "type": "multiple",
                "options": ["grep", "find", "search", "locate"],
                "correct": 0,
                "explanation": "grep padrão arquivo busca linhas que contêm padrão. find busca arquivos."
            },
            {
                "question": "Qual opção grep ignora case?",
                "type": "multiple",
                "options": ["-i", "--ignore-case", "-y", "a e b"],
                "correct": 3,
                "explanation": "grep -i 'palavra' busca ignorando maiúsculas/minúsculas."
            },
            {
                "question": "Qual opção grep mostra número da linha?",
                "type": "multiple",
                "options": ["-n", "-l", "-c", "-v"],
                "correct": 0,
                "explanation": "grep -n mostra número da linha. -l mostra nome do arquivo, -c conta ocorrências."
            },
            {
                "question": "Como buscar recursivamente?",
                "type": "multiple",
                "options": ["grep -r", "grep -R", "rgrep", "Todos anteriores"],
                "correct": 3,
                "explanation": "grep -r 'texto' /diretorio busca em todos arquivos recursivamente."
            },
            {
                "question": "Qual editor de streams?",
                "type": "multiple",
                "options": ["sed", "awk", "ed", "vi"],
                "correct": 0,
                "explanation": "sed 's/antigo/novo/g' substitui texto. sed é Stream EDitor."
            },
            {
                "question": "Qual linguagem de processamento de padrões?",
                "type": "multiple",
                "options": ["awk", "perl", "python", "Todos anteriores"],
                "correct": 3,
                "explanation": "awk especializado em processar texto estruturado em campos."
            },
            {
                "question": "Qual comando mostra diferenças entre arquivos?",
                "type": "multiple",
                "options": ["diff", "cmp", "comm", "Todos anteriores"],
                "correct": 3,
                "explanation": "diff mostra diferenças linha a linha, cmp compara binários, comm compara arquivos ordenados."
            }
        ]
    
    def _get_103_3_questions(self):
        """103.3 Gerenciar processos básicos"""
        return [
            {
                "question": "Qual comando lista processos?",
                "type": "multiple",
                "options": ["ps", "top", "htop", "Todos anteriores"],
                "correct": 3,
                "explanation": "ps lista snapshot, top/htop atualizam em tempo real."
            },
            {
                "question": "Como ver todos processos do sistema?",
                "type": "multiple",
                "options": ["ps aux", "ps -ef", "ps -e", "Todos anteriores"],
                "correct": 3,
                "explanation": "ps aux (BSD style) ou ps -ef (Unix style) mostram todos processos."
            },
            {
                "question": "Qual comando mostra processos em árvore?",
                "type": "multiple",
                "options": ["pstree", "ps -ejH", "ps --forest", "Todos anteriores"],
                "correct": 3,
                "explanation": "pstree mostra hierarquia. ps -ejH ou ps --forest também."
            },
            {
                "question": "Qual sinal termina processo normalmente?",
                "type": "multiple",
                "options": ["SIGTERM (15)", "SIGKILL (9)", "SIGINT (2)", "SIGHUP (1)"],
                "correct": 0,
                "explanation": "SIGTERM permite limpeza. SIGKILL força término imediato."
            },
            {
                "question": "Como enviar sinal a processo?",
                "type": "multiple",
                "options": ["kill", "pkill", "killall", "Todos anteriores"],
                "correct": 3,
                "explanation": "kill por PID, pkill/killall por nome."
            },
            {
                "question": "Como matar processo por nome?",
                "type": "multiple",
                "options": ["pkill processo", "killall processo", "kill -n processo", "a e b"],
                "correct": 3,
                "explanation": "pkill nome ou killall nome terminam processos pelo nome."
            },
            {
                "question": "Como listar sinais disponíveis?",
                "type": "multiple",
                "options": ["kill -l", "signal -l", "man signal", "siglist"],
                "correct": 0,
                "explanation": "kill -l lista todos sinais com números e nomes."
            },
            {
                "question": "Qual variável mostra PID do shell atual?",
                "type": "multiple",
                "options": ["$$", "$PPID", "$!", "$?"],
                "correct": 0,
                "explanation": "$$ é PID do shell atual. $PPID é PID do processo pai."
            },
            {
                "question": "Como ver consumo de recursos?",
                "type": "multiple",
                "options": ["top", "htop", "glances", "Todos anteriores"],
                "correct": 3,
                "explanation": "top básico, htop melhorado, glances mais completo."
            },
            {
                "question": "Como alterar prioridade de processo existente?",
                "type": "multiple",
                "options": ["renice", "nice -p", "chrt", "setpriority"],
                "correct": 0,
                "explanation": "renice -n -5 -p PID aumenta prioridade. Só root pode diminuir nice value."
            },
            {
                "question": "Qual faixa de valores nice?",
                "type": "multiple",
                "options": ["-20 a 19", "0 a 99", "-99 a 99", "1 a 100"],
                "correct": 0,
                "explanation": "-20 é maior prioridade, 19 é menor. Padrão é 0."
            },
            {
                "question": "Como ver processos de usuário específico?",
                "type": "multiple",
                "options": ["ps -u usuario", "top -u usuario", "pgrep -u usuario", "Todos anteriores"],
                "correct": 3,
                "explanation": "ps -u, top -u, pgrep -u mostram processos do usuário."
            },
            {
                "question": "Qual arquivo contém informações de processo?",
                "type": "multiple",
                "options": ["/proc/PID/", "/var/run/", "/tmp/", "/dev/shm/"],
                "correct": 0,
                "explanation": "/proc/PID/ tem diretórios virtuais para cada processo com informações."
            },
            {
                "question": "Como ver arquivos abertos por processo?",
                "type": "multiple",
                "options": ["lsof", "fuser", "pmap", "a e b"],
                "correct": 3,
                "explanation": "lsof -p PID mostra arquivos abertos. fuser mostra processos usando arquivo."
            },
            {
                "question": "Como ver threads de processo?",
                "type": "multiple",
                "options": ["ps -L", "top -H", "htop (modo threads)", "Todos anteriores"],
                "correct": 3,
                "explanation": "ps -L PID mostra threads. top com H alterna para modo threads."
            }
        ]
    
    def _get_103_4_questions(self):
        """103.4 Expressões regulares"""
        return [
            {
                "question": "Qual comando busca arquivos por nome?",
                "type": "multiple",
                "options": ["find", "locate", "which", "Todos anteriores"],
                "correct": 3,
                "explanation": "find busca por critérios, locate usa banco de dados, which mostra caminho de executáveis."
            },
            {
                "question": "Como usar find para buscar por nome?",
                "type": "multiple",
                "options": ["find / -name '*.txt'", "find / -iname '*.TXT'", "find . -name arquivo", "Todos anteriores"],
                "correct": 3,
                "explanation": "find diretorio -name padrão busca arquivos. -iname ignora case."
            },
            {
                "question": "Qual comando usa banco de dados para busca rápida?",
                "type": "multiple",
                "options": ["locate", "find", "whereis", "which"],
                "correct": 0,
                "explanation": "locate arquivo busca em banco de dados updatedb. Mais rápido mas pode estar desatualizado."
            },
            {
                "question": "Como atualizar banco de dados do locate?",
                "type": "multiple",
                "options": ["updatedb", "locate -u", "make locate.db", "refresh-locate"],
                "correct": 0,
                "explanation": "updatedb atualiza banco. Normalmente executado via cron diariamente."
            },
            {
                "question": "Como buscar executáveis no PATH?",
                "type": "multiple",
                "options": ["which", "whereis", "type", "Todos anteriores"],
                "correct": 3,
                "explanation": "which mostra caminho completo, whereis também mostra manpages, type mostra tipo."
            },
            {
                "question": "Como buscar arquivos modificados últimos 7 dias?",
                "type": "multiple",
                "options": ["find / -mtime -7", "find / -newer", "find / -ctime 7", "find / -amin -10080"],
                "correct": 0,
                "explanation": "find / -mtime -7 encontra modificados nos últimos 7 dias. -mtime +7 mais de 7 dias."
            },
            {
                "question": "Como executar comando nos arquivos encontrados?",
                "type": "multiple",
                "options": ["find / -name '*.tmp' -exec rm {} \\;", "find / -name '*.tmp' | xargs rm", "Ambas", "Nenhuma"],
                "correct": 2,
                "explanation": "-exec executa para cada arquivo. xargs é mais eficiente para muitos arquivos."
            },
            {
                "question": "Como buscar arquivos por dono?",
                "type": "multiple",
                "options": ["find / -user root", "find / -group users", "find / -nouser", "Todos anteriores"],
                "correct": 3,
                "explanation": "-user busca por dono, -group por grupo, -nouser arquivos sem dono."
            },
            {
                "question": "Como buscar por tipo (arquivo/diretório)?",
                "type": "multiple",
                "options": ["find / -type f", "find / -type d", "find / -type l", "Todos anteriores"],
                "correct": 3,
                "explanation": "-type f arquivos, d diretórios, l links simbólicos, b dispositivos de bloco, c caracteres."
            },
            {
                "question": "Como buscar arquivos por permissão?",
                "type": "multiple",
                "options": ["find / -perm 644", "find / -perm -u+x", "find / -perm /o+w", "Todos anteriores"],
                "correct": 3,
                "explanation": "-perm 644 permissão exata, -perm -u+x usuário tem execução, /o+w outros têm escrita."
            },
            {
                "question": "Como buscar arquivos por tamanho?",
                "type": "multiple",
                "options": ["find / -size +100M", "find / -size -1G", "find / -empty", "Todos anteriores"],
                "correct": 3,
                "explanation": "-size +100M maiores que 100MB, -1G menores que 1GB, -empty vazios."
            },
            {
                "question": "Como limitar profundidade da busca?",
                "type": "multiple",
                "options": ["find / -maxdepth 2", "find / -mindepth 3", "find / -depth", "a e b"],
                "correct": 3,
                "explanation": "-maxdepth N não vai além de N níveis, -mindepth M começa em nível M."
            },
            {
                "question": "Como buscar manpages por descrição?",
                "type": "multiple",
                "options": ["apropos", "man -k", "whatis", "a e b"],
                "correct": 3,
                "explanation": "apropos palavra ou man -k palavra buscam nas descrições das manpages."
            },
            {
                "question": "Como ver onde estão manpages?",
                "type": "multiple",
                "options": ["manpath", "whereis comando", "whatis comando", "a e b"],
                "correct": 3,
                "explanation": "manpath mostra diretórios de manpages. whereis mostra caminho da manpage."
            },
            {
                "question": "Como buscar links simbólicos quebrados?",
                "type": "multiple",
                "options": ["find / -type l -xtype l", "find -L / -type l", "symlinks -r /", "Todos anteriores"],
                "correct": 3,
                "explanation": "find / -type l ! -exec test -e {} \\; -print também encontra links quebrados."
            }
        ]
    
    def _get_104_1_questions(self):
        """104.1 Criar partições e sistemas de arquivos"""
        return [
            {
                "question": "Qual comando cria sistema de arquivos ext4?",
                "type": "multiple",
                "options": ["mkfs.ext4", "mke2fs -t ext4", "format.ext4", "a e b"],
                "correct": 3,
                "explanation": "mkfs.ext4 /dev/sdb1 ou mke2fs -t ext4 /dev/sdb1 criam ext4."
            },
            {
                "question": "Qual comando cria partição swap?",
                "type": "multiple",
                "options": ["mkswap", "mkfs.swap", "swapcreate", "swapon"],
                "correct": 0,
                "explanation": "mkswap /dev/sda2 formata partição como swap. swapon ativa."
            },
            {
                "question": "Como criar tabela de partição GPT?",
                "type": "multiple",
                "options": ["parted /dev/sda mklabel gpt", "gdisk /dev/sda", "fdisk -g /dev/sda", "a e b"],
                "correct": 3,
                "explanation": "parted ou gdisk criam GPT. fdisk moderno também suporta."
            },
            {
                "question": "Como usar fdisk para criar partição?",
                "type": "multiple",
                "options": ["fdisk /dev/sda, depois n", "cfdisk /dev/sda", "sfdisk /dev/sda", "Todos anteriores"],
                "correct": 3,
                "explanation": "fdisk interativo, cfdisk ncurses, sfdisk scriptável."
            },
            {
                "question": "Como verificar blocos defeituosos?",
                "type": "multiple",
                "options": ["badblocks", "fsck -c", "smartctl -t long", "Todos anteriores"],
                "correct": 3,
                "explanation": "badblocks -v /dev/sda testa blocos. smartctl testa SMART."
            },
            {
                "question": "Qual comando cria sistema de arquivos XFS?",
                "type": "multiple",
                "options": ["mkfs.xfs", "xfs_mkfs", "xfs_admin", "xfs_format"],
                "correct": 0,
                "explanation": "mkfs.xfs /dev/sdb1 cria XFS. -f força se já tiver filesystem."
            },
            {
                "question": "Qual comando verifica sistema de arquivos?",
                "type": "multiple",
                "options": ["fsck", "e2fsck", "xfs_repair", "Todos anteriores"],
                "correct": 3,
                "explanation": "fsck genérico, e2fsck para ext2/3/4, xfs_repair para XFS."
            },
            {
                "question": "Como criar volume lógico LVM?",
                "type": "multiple",
                "options": ["lvcreate", "lvmcreate", "vgcreate", "pvcreate"],
                "correct": 0,
                "explanation": "lvcreate -L 10G -n lv_dados vg_sistema cria logical volume."
            },
            {
                "question": "Como criar volume físico LVM?",
                "type": "multiple",
                "options": ["pvcreate", "pvmk", "initpv", "lvm pvcreate"],
                "correct": 0,
                "explanation": "pvcreate /dev/sda1 inicializa partição como physical volume."
            },
            {
                "question": "Como criar grupo de volumes LVM?",
                "type": "multiple",
                "options": ["vgcreate", "vgextend", "vgmake", "lvm vgcreate"],
                "correct": 0,
                "explanation": "vgcreate vg_nome /dev/sda1 cria volume group."
            },
            {
                "question": "Como estender volume lógico?",
                "type": "multiple",
                "options": ["lvextend", "lvresize", "lvgrow", "a e b"],
                "correct": 3,
                "explanation": "lvextend -L +5G /dev/vg/lv aumenta LV em 5GB."
            },
            {
                "question": "Como redimensionar sistema de arquivos ext4?",
                "type": "multiple",
                "options": ["resize2fs", "e2resize", "ext4grow", "fsck --resize"],
                "correct": 0,
                "explanation": "resize2fs /dev/vg/lv redimensiona após lvextend. resize2fs -p para progresso."
            },
            {
                "question": "Qual comando cria sistema de arquivos Btrfs?",
                "type": "multiple",
                "options": ["mkfs.btrfs", "btrfs-create", "btrfs mkfs", "btrfs format"],
                "correct": 0,
                "explanation": "mkfs.btrfs /dev/sdb1 cria Btrfs. Pode criar com múltiplos dispositivos."
            },
            {
                "question": "Como ver UUID de partição?",
                "type": "multiple",
                "options": ["blkid", "lsblk -f", "tune2fs -l", "Todos anteriores"],
                "correct": 3,
                "explanation": "blkid mostra UUIDs. lsblk -f também. tune2fs -l /dev/sda1 para ext."
            },
            {
                "question": "Como alterar UUID?",
                "type": "multiple",
                "options": ["tune2fs -U random /dev/sda1", "xfs_admin -U generate /dev/sdb1", "btrfstune -U", "Todos anteriores"],
                "correct": 3,
                "explanation": "Cada filesystem tem comando para gerar novo UUID."
            }
        ]
    
    def _get_104_2_questions(self):
        """104.2 Manter integridade de sistemas de arquivos"""
        return [
            {
                "question": "Qual comando verifica sistema de arquivos ext4?",
                "type": "multiple",
                "options": ["fsck.ext4", "e2fsck", "checkfs", "a e b"],
                "correct": 3,
                "explanation": "fsck.ext4 ou e2fsck verificam ext2/3/4. e2fsck -p repara automaticamente."
            },
            {
                "question": "Como forçar verificação no próximo boot?",
                "type": "multiple",
                "options": ["touch /forcefsck", "shutdown -F", "tune2fs -C 1", "a e b"],
                "correct": 3,
                "explanation": "touch /forcefsck (SysV) ou shutdown -F forçam fsck no boot."
            },
            {
                "question": "Como agendar verificação periódica?",
                "type": "multiple",
                "options": ["tune2fs -i 30d /dev/sda1", "tune2fs -c 30 /dev/sda1", "fsck --schedule", "chkfsck"],
                "correct": 0,
                "explanation": "tune2fs -i 30d força verificação após 30 dias desde última."
            },
            {
                "question": "Qual comando verifica XFS?",
                "type": "multiple",
                "options": ["xfs_repair", "xfs_check", "xfs_fsck", "xfs_verify"],
                "correct": 0,
                "explanation": "xfs_repair verifica e repara XFS. Deve estar desmontado ou montado readonly."
            },
            {
                "question": "Como ver informações de superbloco ext4?",
                "type": "multiple",
                "options": ["dumpe2fs", "tune2fs -l", "debugfs", "a e b"],
                "correct": 3,
                "explanation": "dumpe2fs /dev/sda1 mostra informações detalhadas incluindo superbloco backups."
            },
            {
                "question": "Como ver contagem de mounts?",
                "type": "multiple",
                "options": ["tune2fs -l | grep Mount", "dumpe2fs | grep Count", "fsck -l", "mountcount"],
                "correct": 0,
                "explanation": "tune2fs -l mostra 'Mount count' e 'Maximum mount count'."
            },
            {
                "question": "Como desabilitar verificação por contagem de mounts?",
                "type": "multiple",
                "options": ["tune2fs -c 0 /dev/sda1", "tune2fs -i 0", "fsck -D", "noautofsck"],
                "correct": 0,
                "explanation": "tune2fs -c 0 desabilita verificação baseada em contagem."
            },
            {
                "question": "Como restaurar superbloco backup?",
                "type": "multiple",
                "options": ["e2fsck -b 32768 /dev/sda1", "fsck.ext4 -B 32768", "restoresb", "mke2fs -S"],
                "correct": 0,
                "explanation": "e2fsck -b superbloco_backup restaura superbloco. 32768 é backup comum."
            },
            {
                "question": "Como marcar blocos defeituosos automaticamente?",
                "type": "multiple",
                "options": ["e2fsck -c /dev/sda1", "badblocks -n /dev/sda1", "fsck -b", "markbad"],
                "correct": 0,
                "explanation": "e2fsck -c verifica e marca blocos ruins. badblocks testa sem filesystem."
            },
            {
                "question": "Qual campo no /etc/fstab controla verificação no boot?",
                "type": "multiple",
                "options": ["6º campo (pass)", "5º campo (dump)", "4º campo (opções)", "3º campo (tipo)"],
                "correct": 0,
                "explanation": "6º campo: 0=não verifica, 1=raiz, 2=outros filesystems."
            },
            {
                "question": "Como verificar filesystem readonly?",
                "type": "multiple",
                "options": ["fsck -n", "e2fsck -n", "fsck --dry-run", "Todos anteriores"],
                "correct": 3,
                "explanation": "-n faz verificação sem modificar, modo de simulação."
            },
            {
                "question": "Qual comando verifica Btrfs?",
                "type": "multiple",
                "options": ["btrfs check", "btrfsck", "fsck.btrfs", "btrfs-fsck"],
                "correct": 0,
                "explanation": "btrfs check /dev/sda1 verifica Btrfs. --repair para reparar (cuidado!)."
            },
            {
                "question": "Como verificar integridade de dados Btrfs?",
                "type": "multiple",
                "options": ["btrfs scrub start /mnt", "btrfs check --data", "btrfs verify", "btrfs integrity"],
                "correct": 0,
                "explanation": "btrfs scrub verifica e corrige erros de dados em Btrfs montado."
            },
            {
                "question": "Como corrigir automaticamente no fsck?",
                "type": "multiple",
                "options": ["fsck -y", "e2fsck -p", "fsck -a", "Todos anteriores"],
                "correct": 3,
                "explanation": "-y responde yes a tudo, -p repara automaticamente, -a antigo para auto-repair."
            },
            {
                "question": "Como verificar uso de inodes?",
                "type": "multiple",
                "options": ["df -i", "tune2fs -l | grep Inode", "stat -f", "Todos anteriores"],
                "correct": 3,
                "explanation": "df -i mostra uso de inodes. tune2fs -l mostra contagens totais."
            }
        ]
    
    def _get_104_3_questions(self):
        """104.3 Montar e desmontar sistemas de arquivos"""
        return [
            {
                "question": "Qual comando monta sistema de arquivos?",
                "type": "multiple",
                "options": ["mount", "umount", "fsmount", "mnt"],
                "correct": 0,
                "explanation": "mount /dev/sdb1 /mnt monta partição. mount -a monta todos do fstab."
            },
            {
                "question": "Qual comando desmonta?",
                "type": "multiple",
                "options": ["umount", "unmount", "mount -u", "fsunmount"],
                "correct": 0,
                "explanation": "umount /mnt ou umount /dev/sdb1 desmontam."
            },
            {
                "question": "Qual arquivo define montagens automáticas?",
                "type": "multiple",
                "options": ["/etc/fstab", "/etc/mtab", "/proc/mounts", "/etc/filesystems"],
                "correct": 0,
                "explanation": "/etc/fstab: dispositivo ponto_montagem tipo opções dump pass"
            },
            {
                "question": "Como remontar como readonly?",
                "type": "multiple",
                "options": ["mount -o remount,ro /mnt", "mount -o ro /mnt", "remount -r", "a e b"],
                "correct": 3,
                "explanation": "mount -o remount,ro muda para readonly sem desmontar."
            },
            {
                "question": "Como listar sistemas montados?",
                "type": "multiple",
                "options": ["mount", "df", "findmnt", "Todos anteriores"],
                "correct": 3,
                "explanation": "mount lista, df mostra uso de espaço, findmnt mostra em árvore."
            },
            {
                "question": "Como montar usando UUID?",
                "type": "multiple",
                "options": ["mount UUID=xxxx /mnt", "mount /dev/disk/by-uuid/xxxx /mnt", "Ambas", "Nenhuma"],
                "correct": 2,
                "explanation": "Ambas formas montam usando UUID, que é mais estável que nome de dispositivo."
            },
            {
                "question": "Como desmontar sistema ocupado?",
                "type": "multiple",
                "options": ["umount -l", "umount -f", "fuser -km /mnt", "Todos anteriores"],
                "correct": 3,
                "explanation": "-l lazy unmount, -f força, fuser -k mata processos usando o mount."
            },
            {
                "question": "Como ver processos usando mount point?",
                "type": "multiple",
                "options": ["lsof /mnt", "fuser -m /mnt", "ps aux | grep /mnt", "a e b"],
                "correct": 3,
                "explanation": "lsof /mnt ou fuser -m /mnt mostram processos com arquivos abertos no diretório."
            },
            {
                "question": "Qual opção mount desabilita execução?",
                "type": "multiple",
                "options": ["-o noexec", "-o nosuid", "-o nodev", "-o ro"],
                "correct": 0,
                "explanation": "noexec bloqueia execução de binários, nosuid ignora bits SUID, nodev ignora dispositivos."
            },
            {
                "question": "Como montar imagem ISO?",
                "type": "multiple",
                "options": ["mount -o loop arquivo.iso /mnt", "mount arquivo.iso /mnt", "isomount arquivo.iso", "loopmount arquivo.iso"],
                "correct": 0,
                "explanation": "mount -o loop usa dispositivo loopback para montar imagem."
            },
            {
                "question": "Como montar share Windows/Samba?",
                "type": "multiple",
                "options": ["mount -t cifs", "mount -t smbfs", "smbclient", "a e b"],
                "correct": 3,
                "explanation": "mount -t cifs //servidor/share /mnt -o user=nome,password=senha"
            },
            {
                "question": "Como montar NFS?",
                "type": "multiple",
                "options": ["mount -t nfs", "mount.nfs", "nfsmount", "a e b"],
                "correct": 3,
                "explanation": "mount -t nfs servidor:/export /mnt monta share NFS."
            },
            {
                "question": "Como permitir usuários montarem?",
                "type": "multiple",
                "options": ["mount -o user", "mount -o users", "mount -o allow-user", "user-mount"],
                "correct": 1,
                "explanation": "mount -o users no fstab permite qualquer usuário montar/desmontar."
            },
            {
                "question": "Como montar tmpfs (RAM)?",
                "type": "multiple",
                "options": ["mount -t tmpfs tmpfs /mnt/tmp", "mount tmpfs /mnt -o type=tmpfs", "mktmpfs /mnt", "a e b"],
                "correct": 3,
                "explanation": "mount -t tmpfs -o size=1G tmpfs /mnt/tmp cria filesystem em RAM."
            },
            {
                "question": "Qual arquivo mostra filesystems suportados?",
                "type": "multiple",
                "options": ["/proc/filesystems", "/etc/filesystems", "cat /lib/modules/*/modules.* | grep fs", "Todos anteriores"],
                "correct": 3,
                "explanation": "/proc/filesystems mostra filesystems suportados pelo kernel."
            }
        ]
    
    def get_random_questions(self, topic: str, num: int = 10) -> List[Dict]:
        """Retorna questões aleatórias de um tópico específico"""
        if topic in self.questions:
            available = self.questions[topic]
            if num > len(available):
                num = len(available)
            return random.sample(available, num)
        return []
    
    def get_all_topics(self) -> List[str]:
        """Retorna lista de todos os tópicos disponíveis"""
        return list(self.questions.keys())


class LPIC1StudyApp:
    """Aplicativo principal de estudo LPIC-1"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Estudo LPIC-1 - Tópicos 101 a 104")
        self.root.geometry("1000x800")
        
        # Banco de questões
        self.question_bank = QuestionBank()
        
        # Variáveis de controle
        self.current_topic = tk.StringVar()
        self.current_question_index = 0
        self.current_questions = []
        self.score = 0
        self.total_questions = 0
        self.user_answers = {}
        self.question_results = {}  # Armazena se cada questão foi acertada
        
        # Configurar estilo
        self.setup_styles()
        
        # Criar interface
        self.create_widgets()
        
        # Carregar tópicos
        self.load_topics()
        
    def setup_styles(self):
        """Configura estilos da interface"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores
        self.bg_color = "#f0f0f0"
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.correct_color = "#27ae60"
        self.wrong_color = "#e74c3c"
        
        self.root.configure(bg=self.bg_color)
        
        # Configurar estilos personalizados
        style.configure("Title.TLabel", font=("Arial", 20, "bold"), foreground=self.primary_color)
        style.configure("Subtitle.TLabel", font=("Arial", 11))
        style.configure("Question.TLabel", font=("Arial", 12, "bold"))
        style.configure("Correct.TRadiobutton", foreground=self.correct_color)
        style.configure("Wrong.TRadiobutton", foreground=self.wrong_color)
        
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="LPIC-1 Sistema de Estudo", 
            style="Title.TLabel"
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Subtítulo
        subtitle_label = ttk.Label(
            main_frame,
            text="Tópicos 101 a 104 - Preparação para Certificação Linux",
            style="Subtitle.TLabel"
        )
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Frame de controle
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        control_frame.columnconfigure(1, weight=1)
        
        ttk.Label(control_frame, text="Selecione o Tópico:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        
        self.topic_combo = ttk.Combobox(
            control_frame, 
            textvariable=self.current_topic,
            state="readonly",
            width=50
        )
        self.topic_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        self.start_btn = ttk.Button(
            control_frame, 
            text="Iniciar Teste (10 questões)", 
            command=self.start_test,
            width=20
        )
        self.start_btn.grid(row=0, column=2, padx=(5, 0))
        
        # Frame da questão
        self.question_frame = ttk.LabelFrame(main_frame, text="Questão", padding="20")
        self.question_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        self.question_frame.columnconfigure(0, weight=1)
        
        # Número da questão
        self.question_number_label = ttk.Label(
            self.question_frame,
            text="",
            font=("Arial", 10, "bold"),
            foreground=self.primary_color
        )
        self.question_number_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # Texto da questão
        self.question_text = tk.Text(
            self.question_frame, 
            height=4,
            wrap=tk.WORD,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg=self.bg_color,
            padx=10,
            pady=10
        )
        self.question_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Frame de resposta (será configurado dinamicamente)
        self.answer_frame = ttk.Frame(self.question_frame)
        self.answer_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        self.answer_frame.columnconfigure(0, weight=1)
        
        # Frame de botões de navegação
        nav_frame = ttk.Frame(self.question_frame)
        nav_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        self.prev_btn = ttk.Button(
            nav_frame, 
            text="← Anterior", 
            command=self.prev_question,
            state="disabled",
            width=15
        )
        self.prev_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.next_btn = ttk.Button(
            nav_frame, 
            text="Próxima →", 
            command=self.next_question,
            state="disabled",
            width=15
        )
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        self.submit_btn = ttk.Button(
            nav_frame, 
            text="Enviar Resposta", 
            command=self.submit_answer,
            state="disabled",
            width=15
        )
        self.submit_btn.pack(side=tk.LEFT, padx=5)
        
        self.finish_btn = ttk.Button(
            nav_frame,
            text="Finalizar Teste",
            command=self.finish_test,
            state="disabled",
            width=15
        )
        self.finish_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame de explicação
        self.explanation_frame = ttk.LabelFrame(main_frame, text="Explicação", padding="15")
        self.explanation_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.explanation_frame.columnconfigure(0, weight=1)
        self.explanation_frame.rowconfigure(0, weight=1)
        
        self.explanation_text = scrolledtext.ScrolledText(
            self.explanation_frame,
            height=10,
            wrap=tk.WORD,
            font=("Arial", 10),
            relief=tk.FLAT,
            bg=self.bg_color
        )
        self.explanation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Barra de status
        self.status_var = tk.StringVar()
        self.status_var.set("Selecione um tópico e clique em 'Iniciar Teste'")
        
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=(10, 5)
        )
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(15, 0))
        
    def load_topics(self):
        """Carrega a lista de tópicos no combobox"""
        topics = self.question_bank.get_all_topics()
        self.topic_combo['values'] = topics
        if topics:
            self.current_topic.set(topics[0])
    
    def start_test(self):
        """Inicia um novo teste com questões do tópico selecionado"""
        topic = self.current_topic.get()
        if not topic:
            messagebox.showwarning("Aviso", "Selecione um tópico primeiro!")
            return
        
        # Carregar questões
        self.current_questions = self.question_bank.get_random_questions(topic, 10)
        if not self.current_questions:
            messagebox.showwarning("Aviso", f"Nenhuma questão encontrada para {topic}")
            return
        
        # Resetar estado
        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(self.current_questions)
        self.user_answers = {}
        self.question_results = {}
        
        # Atualizar interface
        self.start_btn['state'] = 'disabled'
        self.topic_combo['state'] = 'disabled'
        self.prev_btn['state'] = 'normal'
        self.next_btn['state'] = 'normal'
        self.submit_btn['state'] = 'normal'
        self.finish_btn['state'] = 'normal'
        
        # Mostrar primeira questão
        self.show_question()
        
        # Atualizar status
        self.status_var.set(f"Teste iniciado: {topic} - Questão 1 de {self.total_questions}")
    
    def show_question(self):
        """Mostra a questão atual"""
        # Limpar frames
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        # Limpar explicação
        self.explanation_text.delete(1.0, tk.END)
        
        if self.current_question_index >= len(self.current_questions):
            return
        
        question = self.current_questions[self.current_question_index]
        
        # Atualizar número da questão
        self.question_number_label.config(
            text=f"Questão {self.current_question_index + 1} de {self.total_questions}"
        )
        
        # Mostrar texto da questão
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.insert(1.0, question["question"])
        self.question_text.config(state=tk.DISABLED)
        
        # Configurar tipo de resposta
        if question["type"] == "multiple":
            self.setup_multiple_choice(question)
        elif question["type"] == "text":
            self.setup_text_answer(question)
        
        # Verificar se já respondeu
        if self.current_question_index in self.user_answers:
            self.show_answer_feedback()
        
        # Atualizar navegação
        self.update_navigation()
    
    def setup_multiple_choice(self, question):
        """Configura interface para questão de múltipla escolha"""
        self.user_answer_var = tk.StringVar(value="")
        
        for i, option in enumerate(question["options"]):
            rb = ttk.Radiobutton(
                self.answer_frame,
                text=option,
                variable=self.user_answer_var,
                value=str(i),
                style="TRadiobutton"
            )
            rb.grid(row=i, column=0, sticky=tk.W, pady=3, padx=(0, 10))
        
        # Se já respondeu, marcar a resposta
        if self.current_question_index in self.user_answers:
            self.user_answer_var.set(self.user_answers[self.current_question_index])
    
    def setup_text_answer(self, question):
        """Configura interface para questão de resposta textual"""
        ttk.Label(self.answer_frame, text="Digite sua resposta:").grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5)
        )
        
        self.text_answer_var = tk.StringVar()
        text_entry = ttk.Entry(
            self.answer_frame,
            textvariable=self.text_answer_var,
            width=60
        )
        text_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Se já respondeu, mostrar resposta
        if self.current_question_index in self.user_answers:
            self.text_answer_var.set(self.user_answers[self.current_question_index])
    
    def submit_answer(self):
        """Submete a resposta atual"""
        question = self.current_questions[self.current_question_index]
        user_answer = None
        
        # Obter resposta do usuário
        if question["type"] == "multiple":
            if not self.user_answer_var.get():
                messagebox.showwarning("Aviso", "Selecione uma opção!")
                return
            user_answer = self.user_answer_var.get()
        elif question["type"] == "text":
            if not self.text_answer_var.get().strip():
                messagebox.showwarning("Aviso", "Digite uma resposta!")
                return
            user_answer = self.text_answer_var.get().strip()
        
        # Armazenar resposta
        self.user_answers[self.current_question_index] = user_answer
        
        # Verificar se está correta
        is_correct = False
        if question["type"] == "multiple":
            is_correct = (int(user_answer) == question["correct"])
        elif question["type"] == "text":
            correct_answers = [ans.lower() for ans in question["correct"]]
            is_correct = (user_answer.lower() in correct_answers)
        
        # Armazenar resultado
        self.question_results[self.current_question_index] = is_correct
        
        # Atualizar pontuação total
        self.score = sum(1 for result in self.question_results.values() if result)
        
        # Mostrar feedback
        self.show_answer_feedback()
        
        # Atualizar status
        self.status_var.set(
            f"Resposta submetida. "
            f"Acertos: {self.score}/{self.total_questions} "
            f"({(self.score/self.total_questions*100):.1f}%)"
        )
    
    def show_answer_feedback(self):
        """Mostra feedback da resposta"""
        if self.current_question_index not in self.user_answers:
            return
        
        question = self.current_questions[self.current_question_index]
        user_answer = self.user_answers[self.current_question_index]
        is_correct = self.question_results.get(self.current_question_index, False)
        
        # Determinar resposta correta
        correct_answer = ""
        if question["type"] == "multiple":
            correct_answer = question["options"][question["correct"]]
        elif question["type"] == "text":
            correct_answer = " ou ".join(question["correct"])
        
        # Mostrar explicação
        self.explanation_text.delete(1.0, tk.END)
        
        # Adicionar cabeçalho colorido
        if is_correct:
            self.explanation_text.insert(1.0, "✓ CORRETO\n\n")
            self.explanation_text.tag_add("correct", "1.0", "1.8")
        else:
            self.explanation_text.insert(1.0, "✗ INCORRETO\n\n")
            self.explanation_text.tag_add("wrong", "1.0", "1.10")
        
        # Mostrar resposta correta
        if question["type"] == "multiple":
            user_choice = question["options"][int(user_answer)] if user_answer.isdigit() else user_answer
            self.explanation_text.insert(tk.END, f"Sua resposta: {user_choice}\n")
            self.explanation_text.insert(tk.END, f"Resposta correta: {correct_answer}\n\n")
        elif question["type"] == "text":
            self.explanation_text.insert(tk.END, f"Sua resposta: {user_answer}\n")
            self.explanation_text.insert(tk.END, f"Resposta(s) correta(s): {correct_answer}\n\n")
        
        # Mostrar explicação
        self.explanation_text.insert(tk.END, f"Explicação: {question['explanation']}")
        
        # Configurar tags para cores
        self.explanation_text.tag_config("correct", foreground=self.correct_color, 
                                         font=("Arial", 10, "bold"))
        self.explanation_text.tag_config("wrong", foreground=self.wrong_color, 
                                         font=("Arial", 10, "bold"))
        
        # Destacar widgets de resposta
        if question["type"] == "multiple":
            for widget in self.answer_frame.winfo_children():
                if isinstance(widget, ttk.Radiobutton):
                    widget_value = widget.cget("value")
                    if widget_value == user_answer:
                        if is_correct:
                            widget.configure(style="Correct.TRadiobutton")
                        else:
                            widget.configure(style="Wrong.TRadiobutton")
                    elif widget_value == str(question["correct"]):
                        widget.configure(style="Correct.TRadiobutton")
        
        # Desabilitar submit para esta questão
        self.submit_btn['state'] = 'disabled'
    
    def prev_question(self):
        """Vai para a questão anterior"""
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()
    
    def next_question(self):
        """Vai para a próxima questão"""
        if self.current_question_index < len(self.current_questions) - 1:
            self.current_question_index += 1
            self.show_question()
    
    def update_navigation(self):
        """Atualiza estado dos botões de navegação"""
        self.prev_btn['state'] = 'normal' if self.current_question_index > 0 else 'disabled'
        self.next_btn['state'] = 'normal' if self.current_question_index < len(self.current_questions) - 1 else 'disabled'
        
        # Habilitar submit se ainda não respondeu
        if self.current_question_index in self.user_answers:
            self.submit_btn['state'] = 'disabled'
        else:
            self.submit_btn['state'] = 'normal'
    
    def finish_test(self):
        """Finaliza o teste e mostra resultados"""
        # Contar questões respondidas
        answered = len(self.user_answers)
        
        if answered < self.total_questions:
            if not messagebox.askyesno("Confirmar", 
                                      f"Você respondeu apenas {answered} de {self.total_questions} questões. "
                                      "Deseja finalizar mesmo assim?"):
                return
        
        # Calcular porcentagem
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        
        # Determinar mensagem baseada no desempenho
        if percentage >= 90:
            performance = "Excelente!"
            message = "Você domina completamente este tópico."
        elif percentage >= 70:
            performance = "Bom!"
            message = "Você tem um bom conhecimento, mas pode melhorar em alguns pontos."
        elif percentage >= 50:
            performance = "Regular"
            message = "Recomenda-se estudar mais o material antes do exame."
        else:
            performance = "Precisa melhorar"
            message = "É necessário revisar completamente este tópico."
        
        # Mostrar resultados
        result_msg = (
            f"{performance}\n\n"
            f"Tópico: {self.current_topic.get()}\n"
            f"Total de questões: {self.total_questions}\n"
            f"Questões respondidas: {answered}\n"
            f"Respostas corretas: {self.score}\n"
            f"Porcentagem de acerto: {percentage:.1f}%\n\n"
            f"{message}"
        )
        
        messagebox.showinfo("Resultados do Teste", result_msg)
        
        # Resetar interface
        self.reset_test()
    
    def reset_test(self):
        """Reseta o teste para estado inicial"""
        self.current_question_index = 0
        self.current_questions = []
        self.score = 0
        self.total_questions = 0
        self.user_answers = {}
        self.question_results = {}
        
        # Limpar interface
        self.question_number_label.config(text="")
        
        self.question_text.config(state=tk.NORMAL)
        self.question_text.delete(1.0, tk.END)
        self.question_text.config(state=tk.DISABLED)
        
        self.explanation_text.delete(1.0, tk.END)
        
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
        
        # Resetar botões
        self.start_btn['state'] = 'normal'
        self.topic_combo['state'] = 'readonly'
        self.prev_btn['state'] = 'disabled'
        self.next_btn['state'] = 'disabled'
        self.submit_btn['state'] = 'disabled'
        self.finish_btn['state'] = 'disabled'
        
        self.status_var.set("Selecione um tópico e clique em 'Iniciar Teste'")


def main():
    """Função principal"""
    root = tk.Tk()
    app = LPIC1StudyApp(root)
    
    # Iniciar aplicação
    root.mainloop()


if __name__ == "__main__":
    main()