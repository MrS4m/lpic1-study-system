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
    """Banco de questões LPIC-1"""
    
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
        """Hardware e Arquitetura (101.1)"""
        return [
            {
                "question": "Qual comando lista todos os dispositivos PCI no sistema?",
                "type": "multiple",
                "options": ["lspci", "lsusb", "lshw", "hwinfo"],
                "correct": 0,
                "explanation": "lspci lista todos os dispositivos conectados ao barramento PCI. Funciona em Debian, RedHat, OpenSUSE e outras distribuições."
            },
            {
                "question": "Digite o comando para listar dispositivos USB conectados:",
                "type": "text",
                "correct": ["lsusb"],
                "explanation": "lsusb exibe informações sobre barramentos USB e dispositivos conectados."
            },
            {
                "question": "Qual arquivo contém informações sobre a CPU?",
                "type": "multiple",
                "options": ["/proc/cpuinfo", "/sys/cpu", "/dev/cpu", "/etc/cpuinfo"],
                "correct": 0,
                "explanation": "/proc/cpuinfo é um arquivo virtual que contém informações detalhadas sobre processadores."
            },
            {
                "question": "Digite o diretório onde ficam os arquivos de dispositivos:",
                "type": "text",
                "correct": ["/dev", "dev"],
                "explanation": "/dev contém arquivos especiais que representam dispositivos de hardware."
            },
            {
                "question": "Qual comando exibe informações detalhadas sobre hardware?",
                "type": "multiple",
                "options": ["lshw", "hwlist", "showhard", "hardinfo"],
                "correct": 0,
                "explanation": "lshw (list hardware) exibe informações detalhadas sobre toda a configuração de hardware."
            },
            {
                "question": "Qual arquivo virtual contém informações sobre dispositivos PCI?",
                "type": "multiple",
                "options": ["/proc/pci", "/proc/bus/pci/devices", "/sys/pci", "/dev/pci"],
                "correct": 1,
                "explanation": "/proc/bus/pci/devices lista dispositivos PCI de forma mais detalhada."
            },
            {
                "question": "Digite o comando para ver módulos do kernel carregados:",
                "type": "text",
                "correct": ["lsmod"],
                "explanation": "lsmod lista todos os módulos do kernel atualmente carregados."
            },
            {
                "question": "Qual comando carrega um módulo do kernel?",
                "type": "multiple",
                "options": ["modprobe", "insmod", "loadmod", "kernload"],
                "correct": 0,
                "explanation": "modprobe carrega módulos com suas dependências automaticamente."
            },
            {
                "question": "Digite o comando para remover um módulo do kernel:",
                "type": "text",
                "correct": ["rmmod", "modprobe -r"],
                "explanation": "rmmod remove módulos do kernel. modprobe -r também pode ser usado."
            },
            {
                "question": "Qual diretório contém informações do sistema em tempo real?",
                "type": "multiple",
                "options": ["/proc", "/sys", "/dev", "/run"],
                "correct": 0,
                "explanation": "/proc é um filesystem virtual com informações sobre processos e sistema."
            },
            {
                "question": "Onde ficam os módulos do kernel instalados?",
                "type": "multiple",
                "options": ["/lib/modules", "/usr/lib/modules", "/etc/modules", "/var/modules"],
                "correct": 0,
                "explanation": "/lib/modules/$(uname -r) contém os módulos do kernel da versão atual."
            },
            {
                "question": "Digite o comando para ver informações sobre memória RAM:",
                "type": "text",
                "correct": ["free", "cat /proc/meminfo"],
                "explanation": "free mostra uso de memória. /proc/meminfo tem detalhes completos."
            },
            {
                "question": "Qual utilitário mostra informações sobre dispositivos USB em formato de árvore?",
                "type": "multiple",
                "options": ["lsusb -t", "usbtree", "tree /dev/usb", "usbshow"],
                "correct": 0,
                "explanation": "lsusb -t exibe a hierarquia de dispositivos USB em formato de árvore."
            },
            {
                "question": "Em qual diretório o udev cria links simbólicos para dispositivos?",
                "type": "multiple",
                "options": ["/dev/disk/by-id", "/sys/devices", "/proc/devices", "/etc/udev"],
                "correct": 0,
                "explanation": "udev cria links em /dev/disk/by-id, /dev/disk/by-uuid, etc."
            },
            {
                "question": "Digite o comando para exibir mensagens do kernel:",
                "type": "text",
                "correct": ["dmesg"],
                "explanation": "dmesg exibe mensagens do buffer do kernel, útil para diagnóstico de hardware."
            },
            {
                "question": "Qual arquivo contém IRQs em uso?",
                "type": "multiple",
                "options": ["/proc/interrupts", "/sys/irq", "/dev/irq", "/etc/interrupts"],
                "correct": 0,
                "explanation": "/proc/interrupts mostra interrupções (IRQs) e estatísticas de uso."
            },
            {
                "question": "Qual comando mostra portas I/O em uso?",
                "type": "multiple",
                "options": ["cat /proc/ioports", "lsio", "ioports", "showio"],
                "correct": 0,
                "explanation": "/proc/ioports lista as regiões de I/O registradas."
            },
            {
                "question": "Digite o comando para ver canais DMA em uso:",
                "type": "text",
                "correct": ["cat /proc/dma"],
                "explanation": "/proc/dma mostra os canais DMA (Direct Memory Access) registrados."
            },
            {
                "question": "Qual diretório contém regras do udev no RedHat/CentOS?",
                "type": "multiple",
                "options": ["/etc/udev/rules.d", "/usr/lib/udev", "/lib/udev", "/var/udev"],
                "correct": 0,
                "explanation": "/etc/udev/rules.d contém regras personalizadas do udev em todas as distros."
            },
            {
                "question": "Qual comando recarrega as regras do udev?",
                "type": "multiple",
                "options": ["udevadm control --reload", "udevreload", "reload-udev", "udev-reload"],
                "correct": 0,
                "explanation": "udevadm control --reload recarrega as regras do udev sem reiniciar."
            },
            {
                "question": "Digite o comando para verificar informações detalhadas de um dispositivo com udev:",
                "type": "text",
                "correct": ["udevadm info"],
                "explanation": "udevadm info exibe informações detalhadas sobre dispositivos."
            },
            {
                "question": "Qual arquivo em OpenSUSE lista módulos a serem carregados no boot?",
                "type": "multiple",
                "options": ["/etc/modules-load.d/*.conf", "/etc/modules", "/etc/modprobe.conf", "/etc/sysconfig/modules"],
                "correct": 0,
                "explanation": "OpenSUSE (systemd) usa /etc/modules-load.d/*.conf para carregar módulos."
            },
            {
                "question": "Em qual arquivo você configura opções para módulos do kernel?",
                "type": "multiple",
                "options": ["/etc/modprobe.d/*.conf", "/etc/modules.conf", "/etc/kernel/modules", "/lib/modprobe.d"],
                "correct": 0,
                "explanation": "/etc/modprobe.d/*.conf contém configurações de parâmetros dos módulos."
            },
            {
                "question": "Digite o comando para obter informações sobre um módulo específico:",
                "type": "text",
                "correct": ["modinfo"],
                "explanation": "modinfo exibe informações sobre um módulo do kernel."
            },
            {
                "question": "Qual comando força o sistema a detectar novo hardware?",
                "type": "multiple",
                "options": ["udevadm trigger", "hwdetect", "detect-hardware", "rescan"],
                "correct": 0,
                "explanation": "udevadm trigger força o udev a processar eventos de dispositivos novamente."
            },
        ]
    
    def _get_101_2_questions(self):
        """Boot do Sistema (101.2)"""
        return [
            {
                "question": "Qual é o primeiro processo iniciado pelo kernel Linux?",
                "type": "multiple",
                "options": ["init ou systemd", "bash", "login", "getty"],
                "correct": 0,
                "explanation": "O processo init (PID 1) ou systemd é o primeiro processo iniciado pelo kernel."
            },
            {
                "question": "Digite o comando para listar todos os targets do systemd:",
                "type": "text",
                "correct": ["systemctl list-units --type=target", "systemctl list-units -t target"],
                "explanation": "systemctl list-units --type=target lista todos os targets disponíveis."
            },
            {
                "question": "Qual runlevel corresponde ao modo multiusuário com rede no SysV init?",
                "type": "multiple",
                "options": ["3", "2", "5", "4"],
                "correct": 0,
                "explanation": "Runlevel 3 é modo multiusuário completo com rede, sem interface gráfica."
            },
            {
                "question": "Digite o target systemd equivalente ao runlevel 5:",
                "type": "text",
                "correct": ["graphical.target"],
                "explanation": "graphical.target é equivalente ao runlevel 5 (modo gráfico multiusuário)."
            },
            {
                "question": "Qual arquivo contém o runlevel padrão em sistemas SysV (RedHat antigo)?",
                "type": "multiple",
                "options": ["/etc/inittab", "/etc/init.d/rc", "/etc/default/grub", "/boot/grub/grub.cfg"],
                "correct": 0,
                "explanation": "/etc/inittab define o runlevel padrão em sistemas SysV init."
            },
            {
                "question": "Digite o comando para alterar o target padrão do systemd:",
                "type": "text",
                "correct": ["systemctl set-default"],
                "explanation": "systemctl set-default <target> define o target padrão de boot."
            },
            {
                "question": "Qual comando mostra o target atual do systemd?",
                "type": "multiple",
                "options": ["systemctl get-default", "systemctl show-target", "systemctl current", "systemctl default"],
                "correct": 0,
                "explanation": "systemctl get-default exibe o target padrão configurado."
            },
            {
                "question": "Onde ficam os scripts de inicialização SysV em Debian/Ubuntu?",
                "type": "multiple",
                "options": ["/etc/init.d/", "/etc/rc.d/", "/etc/init/", "/etc/sysv/"],
                "correct": 0,
                "explanation": "/etc/init.d/ contém scripts de inicialização em Debian e derivados."
            },
            {
                "question": "Digite o diretório de scripts SysV no RedHat/CentOS:",
                "type": "text",
                "correct": ["/etc/rc.d/init.d/", "/etc/init.d/"],
                "explanation": "RedHat usa /etc/rc.d/init.d/ (com link em /etc/init.d/)."
            },
            {
                "question": "Qual comando em OpenSUSE/RedHat habilita um serviço SysV no boot?",
                "type": "multiple",
                "options": ["chkconfig <serviço> on", "service enable", "rc-update add", "sysv-enable"],
                "correct": 0,
                "explanation": "chkconfig gerencia serviços SysV em RedHat e OpenSUSE antigos."
            },
            {
                "question": "Digite o comando para listar serviços habilitados no systemd:",
                "type": "text",
                "correct": ["systemctl list-unit-files --state=enabled", "systemctl list-unit-files | grep enabled"],
                "explanation": "systemctl list-unit-files --state=enabled mostra serviços habilitados."
            },
            {
                "question": "Qual parâmetro de kernel força boot em modo single-user no GRUB?",
                "type": "multiple",
                "options": ["single", "1", "s", "Todas as anteriores"],
                "correct": 3,
                "explanation": "single, 1 ou s podem ser usados para boot em modo monousuário."
            },
            {
                "question": "Em qual arquivo você configura parâmetros permanentes do GRUB2?",
                "type": "multiple",
                "options": ["/etc/default/grub", "/boot/grub/grub.cfg", "/etc/grub.conf", "/boot/grub2/grub.cfg"],
                "correct": 0,
                "explanation": "/etc/default/grub contém configurações. grub.cfg é gerado automaticamente."
            },
            {
                "question": "Digite o comando para atualizar o GRUB2 em Debian/Ubuntu:",
                "type": "text",
                "correct": ["update-grub", "grub-mkconfig -o /boot/grub/grub.cfg"],
                "explanation": "update-grub (ou grub-mkconfig) regenera a configuração do GRUB2."
            },
            {
                "question": "Qual comando atualiza GRUB2 em RedHat/CentOS 7+?",
                "type": "multiple",
                "options": ["grub2-mkconfig -o /boot/grub2/grub.cfg", "update-grub", "grub-install", "grub2-update"],
                "correct": 0,
                "explanation": "RedHat usa grub2-mkconfig e o caminho /boot/grub2/grub.cfg."
            },
            {
                "question": "Digite o comando systemd para isolar (mudar para) um target:",
                "type": "text",
                "correct": ["systemctl isolate"],
                "explanation": "systemctl isolate <target> muda para o target especificado imediatamente."
            },
            {
                "question": "Qual tecla você pressiona no GRUB para editar parâmetros de boot?",
                "type": "multiple",
                "options": ["e", "a", "c", "Esc"],
                "correct": 0,
                "explanation": "A tecla 'e' permite editar parâmetros de boot no GRUB2."
            },
            {
                "question": "Onde o systemd armazena unit files do sistema no OpenSUSE?",
                "type": "multiple",
                "options": ["/usr/lib/systemd/system/", "/etc/systemd/system/", "/lib/systemd/", "/var/systemd/"],
                "correct": 0,
                "explanation": "/usr/lib/systemd/system/ contém units do sistema. /etc/systemd/system/ para customizações."
            },
            {
                "question": "Digite o comando para verificar o status de um serviço no systemd:",
                "type": "text",
                "correct": ["systemctl status"],
                "explanation": "systemctl status <serviço> mostra status detalhado de um serviço."
            },
            {
                "question": "Qual arquivo de configuração do GRUB Legacy (antigo) era usado no RedHat?",
                "type": "multiple",
                "options": ["/boot/grub/grub.conf", "/etc/grub.conf", "/boot/grub/menu.lst", "/etc/default/grub"],
                "correct": 0,
                "explanation": "GRUB Legacy no RedHat usava /boot/grub/grub.conf (link para /etc/grub.conf)."
            },
            {
                "question": "Digite o runlevel para modo de resgate (rescue):",
                "type": "text",
                "correct": ["1", "s", "single"],
                "explanation": "Runlevel 1, s ou single é o modo de resgate/monousuário."
            },
            {
                "question": "Qual comando mostra o journal do systemd?",
                "type": "multiple",
                "options": ["journalctl", "systemctl log", "systemd-log", "logctl"],
                "correct": 0,
                "explanation": "journalctl exibe logs do systemd journal."
            },
            {
                "question": "Em qual diretório ficam os links simbólicos de runlevels no SysV?",
                "type": "multiple",
                "options": ["/etc/rc[0-6].d/", "/etc/init.d/rc", "/var/run/rc", "/usr/lib/rc"],
                "correct": 0,
                "explanation": "/etc/rc0.d/, /etc/rc1.d/, etc. contêm links para scripts de cada runlevel."
            },
            {
                "question": "Digite o comando para reiniciar o sistema com systemd:",
                "type": "text",
                "correct": ["systemctl reboot", "reboot"],
                "explanation": "systemctl reboot ou simplesmente reboot reinicia o sistema."
            },
            {
                "question": "Qual target do systemd corresponde ao runlevel 3?",
                "type": "multiple",
                "options": ["multi-user.target", "rescue.target", "graphical.target", "network.target"],
                "correct": 0,
                "explanation": "multi-user.target é equivalente ao runlevel 3 (multiusuário sem GUI)."
            },
        ]
    
    def _get_101_3_questions(self):
        """Runlevels e Shutdown (101.3)"""
        return [
            {
                "question": "Digite o comando para desligar o sistema imediatamente:",
                "type": "text",
                "correct": ["shutdown -h now", "poweroff", "halt"],
                "explanation": "shutdown -h now, poweroff ou halt desligam o sistema imediatamente."
            },
            {
                "question": "Qual comando agenda um shutdown para daqui 10 minutos?",
                "type": "multiple",
                "options": ["shutdown -h +10", "shutdown 10", "poweroff +10", "halt +10"],
                "correct": 0,
                "explanation": "shutdown -h +10 agenda desligamento para 10 minutos no futuro."
            },
            {
                "question": "Digite o comando para cancelar um shutdown agendado:",
                "type": "text",
                "correct": ["shutdown -c"],
                "explanation": "shutdown -c cancela um shutdown previamente agendado."
            },
            {
                "question": "Qual comando reinicia o sistema imediatamente?",
                "type": "multiple",
                "options": ["reboot", "shutdown -r now", "systemctl reboot", "Todas as anteriores"],
                "correct": 3,
                "explanation": "reboot, shutdown -r now e systemctl reboot reiniciam o sistema."
            },
            {
                "question": "Em sistemas SysV, qual comando muda o runlevel?",
                "type": "multiple",
                "options": ["init", "telinit", "runlevel", "Ambas a e b"],
                "correct": 3,
                "explanation": "init e telinit (que é link para init) mudam o runlevel."
            },
            {
                "question": "Digite o comando para ver o runlevel atual e anterior:",
                "type": "text",
                "correct": ["runlevel"],
                "explanation": "runlevel mostra o runlevel anterior e atual (ex: N 5)."
            },
            {
                "question": "Qual sinal (signal) o shutdown envia aos processos antes de desligar?",
                "type": "multiple",
                "options": ["SIGTERM", "SIGKILL", "SIGHUP", "SIGINT"],
                "correct": 0,
                "explanation": "SIGTERM é enviado primeiro, permitindo término gracioso dos processos."
            },
            {
                "question": "Digite o comando systemd para desligar o sistema:",
                "type": "text",
                "correct": ["systemctl poweroff"],
                "explanation": "systemctl poweroff desliga o sistema usando systemd."
            },
            {
                "question": "Qual opção do shutdown envia mensagem aos usuários logados?",
                "type": "multiple",
                "options": ["Mensagem após o tempo", "shutdown -m", "shutdown --message", "shutdown --warn"],
                "correct": 0,
                "explanation": "A mensagem é especificada após o tempo: shutdown +10 'Manutenção em 10min'."
            },
            {
                "question": "Em qual arquivo você pode configurar mensagem de shutdown?",
                "type": "multiple",
                "options": ["/etc/shutdown.allow", "/run/nologin", "/etc/nologin.txt", "/var/run/shutdown"],
                "correct": 1,
                "explanation": "/run/nologin é criado durante shutdown, impedindo novos logins."
            },
            {
                "question": "Digite o comando para entrar em modo de hibernação:",
                "type": "text",
                "correct": ["systemctl hibernate"],
                "explanation": "systemctl hibernate coloca o sistema em hibernação (salva RAM em disco)."
            },
            {
                "question": "Qual comando coloca o sistema em modo de suspensão (sleep)?",
                "type": "multiple",
                "options": ["systemctl suspend", "suspend", "sleep", "pm-suspend"],
                "correct": 0,
                "explanation": "systemctl suspend coloca o sistema em modo de suspensão (RAM ativa)."
            },
            {
                "question": "Qual runlevel desliga o sistema?",
                "type": "multiple",
                "options": ["0", "6", "1", "5"],
                "correct": 0,
                "explanation": "Runlevel 0 desliga o sistema. Runlevel 6 reinicia."
            },
            {
                "question": "Digite o comando para forçar verificação de disco no próximo boot:",
                "type": "text",
                "correct": ["touch /forcefsck", "shutdown -F -r now"],
                "explanation": "touch /forcefsck ou shutdown -F força fsck no próximo boot (sistemas antigos)."
            },
            {
                "question": "Qual comando do systemd mostra unidades que falharam?",
                "type": "multiple",
                "options": ["systemctl --failed", "systemctl list-failed", "systemctl show-failed", "journalctl --failed"],
                "correct": 0,
                "explanation": "systemctl --failed lista units que falharam ao iniciar."
            },
            {
                "question": "Em OpenSUSE com systemd, onde ficam os targets customizados?",
                "type": "multiple",
                "options": ["/etc/systemd/system/", "/usr/lib/systemd/", "/lib/systemd/", "/var/systemd/"],
                "correct": 0,
                "explanation": "/etc/systemd/system/ é para units e targets customizados."
            },
            {
                "question": "Digite o comando para enviar ACPI power button event:",
                "type": "text",
                "correct": ["systemctl poweroff", "acpid"],
                "explanation": "systemctl poweroff simula o pressionamento do botão power via ACPI."
            },
            {
                "question": "Qual arquivo em Debian define o comportamento do Ctrl+Alt+Del?",
                "type": "multiple",
                "options": ["/etc/inittab (SysV) ou systemd unit", "/etc/shutdown.conf", "/etc/init/control-alt-delete.conf", "/etc/default/keyboard"],
                "correct": 0,
                "explanation": "Em SysV é /etc/inittab. No systemd é ctrl-alt-del.target."
            },
            {
                "question": "Digite o comando wall para enviar mensagem a todos os usuários:",
                "type": "text",
                "correct": ["wall"],
                "explanation": "wall envia mensagem broadcast para todos os usuários logados."
            },
            {
                "question": "Qual comando mostra quanto tempo o sistema está ligado?",
                "type": "multiple",
                "options": ["uptime", "whoami", "who -b", "last reboot"],
                "correct": 0,
                "explanation": "uptime mostra há quanto tempo o sistema está rodando e carga média."
            },
            {
                "question": "Em qual diretório ficam as unit files de usuário no systemd?",
                "type": "multiple",
                "options": ["~/.config/systemd/user/", "/etc/systemd/user/", "/home/systemd/", "/var/user/systemd/"],
                "correct": 0,
                "explanation": "~/.config/systemd/user/ contém units específicas do usuário."
            },
            {
                "question": "Digite o comando para recarregar configuração do systemd:",
                "type": "text",
                "correct": ["systemctl daemon-reload"],
                "explanation": "systemctl daemon-reload recarrega configurações de unit files."
            },
            {
                "question": "Qual parâmetro do kernel desabilita modo quiet na inicialização?",
                "type": "multiple",
                "options": ["Remover quiet", "verbose", "debug", "noquiet"],
                "correct": 0,
                "explanation": "Remover 'quiet' dos parâmetros do kernel mostra mensagens detalhadas de boot."
            },
            {
                "question": "Digite o comando para ver dependências de uma unit do systemd:",
                "type": "text",
                "correct": ["systemctl list-dependencies"],
                "explanation": "systemctl list-dependencies <unit> mostra árvore de dependências."
            },
            {
                "question": "Qual comando mostra o tempo de boot de cada serviço no systemd?",
                "type": "multiple",
                "options": ["systemd-analyze blame", "systemctl boot-time", "journalctl --boot-time", "systemd-boottime"],
                "correct": 0,
                "explanation": "systemd-analyze blame lista serviços por tempo de inicialização."
            },
        ]
    
    def _get_102_1_questions(self):
        """Design de Layout de Disco (102.1)"""
        return [
            {
                "question": "Qual diretório deve estar em partição separada para facilitar backup?",
                "type": "multiple",
                "options": ["/home", "/bin", "/etc", "/dev"],
                "correct": 0,
                "explanation": "/home em partição separada facilita reinstalação e backup de dados de usuários."
            },
            {
                "question": "Digite o ponto de montagem que deve ter partição swap:",
                "type": "text",
                "correct": ["swap", "nenhum", "n/a"],
                "explanation": "Swap não tem ponto de montagem, é área de troca (memória virtual)."
            },
            {
                "question": "Qual o tamanho recomendado mínimo para partição /boot?",
                "type": "multiple",
                "options": ["250-500 MB", "50 MB", "1 GB", "10 GB"],
                "correct": 0,
                "explanation": "/boot geralmente precisa de 250-500MB para múltiplos kernels."
            },
            {
                "question": "Em sistemas UEFI, qual partição é obrigatória?",
                "type": "multiple",
                "options": ["EFI System Partition (ESP)", "/boot", "swap", "BIOS Boot"],
                "correct": 0,
                "explanation": "ESP (EFI System Partition) é obrigatória em sistemas UEFI, geralmente ~500MB FAT32."
            },
            {
                "question": "Digite o tipo de tabela de partição para discos > 2TB:",
                "type": "text",
                "correct": ["gpt", "GPT"],
                "explanation": "GPT (GUID Partition Table) suporta discos maiores que 2TB, MBR não."
            },
            {
                "question": "Quantas partições primárias o MBR suporta?",
                "type": "multiple",
                "options": ["4", "3", "Ilimitadas", "128"],
                "correct": 0,
                "explanation": "MBR suporta 4 partições primárias, ou 3 primárias + 1 estendida."
            },
            {
                "question": "Digite o comando para criar partições interativamente:",
                "type": "text",
                "correct": ["fdisk", "cfdisk", "parted"],
                "explanation": "fdisk (texto), cfdisk (ncurses) ou parted podem criar partições."
            },
            {
                "question": "Qual diretório contém logs e deve ter espaço adequado?",
                "type": "multiple",
                "options": ["/var", "/tmp", "/opt", "/usr"],
                "correct": 0,
                "explanation": "/var contém logs, spools e dados variáveis que crescem ao longo do tempo."
            },
            {
                "question": "Em servidores de banco de dados, qual diretório deve ter partição própria?",
                "type": "multiple",
                "options": ["/var ou /home", "/boot", "/tmp", "/etc"],
                "correct": 0,
                "explanation": "Dados de BD geralmente ficam em /var/lib ou /home, precisam partição dedicada."
            },
            {
                "question": "Digite o sistema de arquivos recomendado para ESP (EFI):",
                "type": "text",
                "correct": ["vfat", "fat32", "FAT32"],
                "explanation": "EFI System Partition deve usar FAT32 (vfat no Linux)."
            },
            {
                "question": "Qual ferramenta é recomendada para particionar discos GPT?",
                "type": "multiple",
                "options": ["gdisk ou parted", "fdisk", "cfdisk", "sfdisk"],
                "correct": 0,
                "explanation": "gdisk e parted trabalham bem com GPT. fdisk moderno também suporta."
            },
            {
                "question": "Quantas partições o GPT suporta por padrão?",
                "type": "multiple",
                "options": ["128", "4", "256", "Ilimitadas"],
                "correct": 0,
                "explanation": "GPT suporta até 128 partições por padrão (pode ser mais)."
            },
            {
                "question": "Digite o tipo de código para partição swap no fdisk:",
                "type": "text",
                "correct": ["82", "swap"],
                "explanation": "Tipo 82 é swap no MBR. No GPT use código específico de swap."
            },
            {
                "question": "Qual o código de partição Linux padrão no fdisk (MBR)?",
                "type": "multiple",
                "options": ["83", "82", "8e", "fd"],
                "correct": 0,
                "explanation": "Tipo 83 é Linux filesystem padrão no MBR."
            },
            {
                "question": "Para LVM, qual tipo de partição usar no fdisk?",
                "type": "multiple",
                "options": ["8e (Linux LVM)", "83", "82", "fd"],
                "correct": 0,
                "explanation": "Tipo 8e identifica partições para LVM."
            },
            {
                "question": "Digite o comando para listar partições de todos os discos:",
                "type": "text",
                "correct": ["fdisk -l", "lsblk", "parted -l"],
                "explanation": "fdisk -l lista todas as partições. lsblk mostra em formato de árvore."
            },
            {
                "question": "Qual diretório não deve estar em partição separada?",
                "type": "multiple",
                "options": ["/bin e /lib", "/home", "/var", "/tmp"],
                "correct": 0,
                "explanation": "/bin, /sbin, /lib são necessários antes de montar outras partições."
            },
            {
                "question": "Em sistemas com pouca RAM, qual o tamanho recomendado de swap?",
                "type": "multiple",
                "options": ["1.5-2x a RAM", "Igual à RAM", "Metade da RAM", "Não precisa"],
                "correct": 0,
                "explanation": "Para hibernação e pouca RAM, recomenda-se swap de 1.5-2x o tamanho da RAM."
            },
            {
                "question": "Digite o comando para ver uso de espaço por partição:",
                "type": "text",
                "correct": ["df", "df -h"],
                "explanation": "df mostra uso de espaço. df -h mostra em formato human-readable."
            },
            {
                "question": "Qual partição é usada para BIOS Boot em GPT com GRUB?",
                "type": "multiple",
                "options": ["BIOS Boot Partition (1-2MB)", "ESP", "/boot", "swap"],
                "correct": 0,
                "explanation": "BIOS Boot Partition (~1MB) é necessária para GRUB em sistemas GPT+BIOS."
            },
            {
                "question": "Para RAID por software, qual tipo de partição usar?",
                "type": "multiple",
                "options": ["fd (Linux RAID)", "83", "8e", "82"],
                "correct": 0,
                "explanation": "Tipo fd identifica partições para RAID por software Linux."
            },
            {
                "question": "Digite o ponto de montagem típico para EFI System Partition:",
                "type": "text",
                "correct": ["/boot/efi", "/efi"],
                "explanation": "/boot/efi é o ponto de montagem padrão para ESP na maioria das distros."
            },
            {
                "question": "Qual comando mostra árvore de dispositivos de bloco?",
                "type": "multiple",
                "options": ["lsblk", "tree /dev", "blktree", "blockdev"],
                "correct": 0,
                "explanation": "lsblk lista dispositivos de bloco em formato de árvore com pontos de montagem."
            },
            {
                "question": "Em ambiente de servidor web, qual diretório pode precisar de partição grande?",
                "type": "multiple",
                "options": ["/var/www ou /srv", "/usr", "/opt", "/etc"],
                "correct": 0,
                "explanation": "/var/www ou /srv armazenam conteúdo web e podem precisar muito espaço."
            },
            {
                "question": "Digite o tamanho mínimo recomendado para partição raiz (/):",
                "type": "text",
                "correct": ["15-20", "20", "15", "10-20"],
                "explanation": "Partição raiz precisa de pelo menos 15-20GB para sistema e aplicativos básicos."
            },
        ]
    
    def _get_102_2_questions(self):
        """Instalação de Gerenciador de Boot (102.2)"""
        return [
            {
                "question": "Qual comando instala o GRUB2 no MBR do disco /dev/sda?",
                "type": "multiple",
                "options": ["grub-install /dev/sda", "grub-setup /dev/sda", "install-grub /dev/sda", "grub2-mkconfig"],
                "correct": 0,
                "explanation": "grub-install /dev/sda instala GRUB2 no MBR (não use /dev/sda1)."
            },
            {
                "question": "Digite o comando GRUB2 no RedHat/CentOS para instalar no disco:",
                "type": "text",
                "correct": ["grub2-install"],
                "explanation": "RedHat usa grub2-install ao invés de grub-install."
            },
            {
                "question": "Onde o GRUB2 armazena seus módulos no Debian/Ubuntu?",
                "type": "multiple",
                "options": ["/boot/grub/", "/usr/lib/grub/", "/lib/grub/", "/etc/grub.d/"],
                "correct": 0,
                "explanation": "/boot/grub/ contém módulos e arquivos de configuração do GRUB2."
            },
            {
                "question": "Digite o arquivo de configuração principal do GRUB2:",
                "type": "text",
                "correct": ["/boot/grub/grub.cfg", "/boot/grub2/grub.cfg"],
                "explanation": "/boot/grub/grub.cfg (Debian) ou /boot/grub2/grub.cfg (RedHat)."
            },
            {
                "question": "Qual comando regenera o arquivo de configuração do GRUB2?",
                "type": "multiple",
                "options": ["grub-mkconfig", "update-grub", "grub2-mkconfig", "Todas as anteriores"],
                "correct": 3,
                "explanation": "update-grub (Debian), grub-mkconfig ou grub2-mkconfig (RedHat) geram grub.cfg."
            },
            {
                "question": "Em qual arquivo você define timeout padrão do GRUB2?",
                "type": "multiple",
                "options": ["/etc/default/grub", "/boot/grub/grub.cfg", "/etc/grub.conf", "/boot/grub/menu.lst"],
                "correct": 0,
                "explanation": "/etc/default/grub contém GRUB_TIMEOUT e outras configurações."
            },
            {
                "question": "Digite a variável que define timeout do menu GRUB:",
                "type": "text",
                "correct": ["GRUB_TIMEOUT"],
                "explanation": "GRUB_TIMEOUT em /etc/default/grub define segundos de espera no menu."
            },
            {
                "question": "Qual variável oculta o menu GRUB se houver apenas um sistema?",
                "type": "multiple",
                "options": ["GRUB_TIMEOUT_STYLE=hidden", "GRUB_HIDDEN", "GRUB_DISABLE_MENU", "GRUB_QUIET"],
                "correct": 0,
                "explanation": "GRUB_TIMEOUT_STYLE=hidden oculta menu com um único SO."
            },
            {
                "question": "Em sistemas UEFI, onde o GRUB2 instala o bootloader?",
                "type": "multiple",
                "options": ["EFI System Partition (ESP)", "MBR", "/boot", "NVRAM"],
                "correct": 0,
                "explanation": "Em UEFI, GRUB instala em /boot/efi (ESP), não no MBR."
            },
            {
                "question": "Digite o comando para listar entradas de boot UEFI:",
                "type": "text",
                "correct": ["efibootmgr"],
                "explanation": "efibootmgr lista e gerencia entradas de boot UEFI."
            },
            {
                "question": "Qual diretório contém scripts que geram o grub.cfg?",
                "type": "multiple",
                "options": ["/etc/grub.d/", "/boot/grub.d/", "/usr/lib/grub.d/", "/var/grub.d/"],
                "correct": 0,
                "explanation": "/etc/grub.d/ contém scripts numerados que geram grub.cfg."
            },
            {
                "question": "Digite o script em /etc/grub.d/ que detecta outros sistemas operacionais:",
                "type": "text",
                "correct": ["30_os-prober", "os-prober"],
                "explanation": "30_os-prober detecta outros SOs (Windows, etc) para dual-boot."
            },
            {
                "question": "Qual variável em /etc/default/grub define parâmetros do kernel?",
                "type": "multiple",
                "options": ["GRUB_CMDLINE_LINUX", "GRUB_KERNEL_PARAMS", "GRUB_LINUX_OPTS", "GRUB_BOOT_ARGS"],
                "correct": 0,
                "explanation": "GRUB_CMDLINE_LINUX define parâmetros passados ao kernel."
            },
            {
                "question": "Em GRUB Legacy, qual era o arquivo de configuração?",
                "type": "multiple",
                "options": ["/boot/grub/menu.lst ou grub.conf", "/etc/grub.conf", "/boot/grub/grub.cfg", "/etc/default/grub"],
                "correct": 0,
                "explanation": "GRUB Legacy usava menu.lst (Debian) ou grub.conf (RedHat)."
            },
            {
                "question": "Digite o comando GRUB Legacy para instalar no MBR:",
                "type": "text",
                "correct": ["grub-install", "grub"],
                "explanation": "grub-install também existia no GRUB Legacy."
            },
            {
                "question": "Qual comando no prompt do GRUB2 carrega um módulo?",
                "type": "multiple",
                "options": ["insmod", "module load", "modprobe", "load"],
                "correct": 0,
                "explanation": "insmod carrega módulos no shell do GRUB2."
            },
            {
                "question": "Digite o comando GRUB2 para listar dispositivos disponíveis:",
                "type": "text",
                "correct": ["ls"],
                "explanation": "ls no shell GRUB lista dispositivos e partições disponíveis."
            },
            {
                "question": "Como o GRUB2 referencia o primeiro disco?",
                "type": "multiple",
                "options": ["(hd0)", "(sda)", "(disk0)", "(0)"],
                "correct": 0,
                "explanation": "GRUB usa (hd0) para primeiro disco, (hd0,1) para primeira partição."
            },
            {
                "question": "Qual variável desabilita submenu no GRUB2?",
                "type": "multiple",
                "options": ["GRUB_DISABLE_SUBMENU=y", "GRUB_NO_SUBMENU=true", "GRUB_FLAT_MENU=yes", "GRUB_SIMPLE=true"],
                "correct": 0,
                "explanation": "GRUB_DISABLE_SUBMENU=y desabilita submenus de kernels antigos."
            },
            {
                "question": "Digite o comando para testar configuração GRUB sem instalar:",
                "type": "text",
                "correct": ["grub-mkconfig", "grub2-mkconfig"],
                "explanation": "grub-mkconfig sem -o mostra saída sem salvar, útil para testar."
            },
            {
                "question": "Em OpenSUSE, onde fica o grub.cfg?",
                "type": "multiple",
                "options": ["/boot/grub2/grub.cfg", "/boot/grub/grub.cfg", "/etc/grub2/grub.cfg", "/boot/efi/grub.cfg"],
                "correct": 0,
                "explanation": "OpenSUSE usa /boot/grub2/grub.cfg como RedHat."
            },
            {
                "question": "Qual parâmetro força modo de texto no boot?",
                "type": "multiple",
                "options": ["text ou 3", "nomodeset", "vga=text", "console=tty"],
                "correct": 0,
                "explanation": "Adicionar 'text' ou '3' nos parâmetros inicia em modo texto."
            },
            {
                "question": "Digite a tecla no GRUB2 para acessar linha de comando:",
                "type": "text",
                "correct": ["c"],
                "explanation": "Tecla 'c' abre o shell/linha de comando do GRUB2."
            },
            {
                "question": "Qual arquivo especifica ordem de busca de boot no GRUB Legacy?",
                "type": "multiple",
                "options": ["device.map", "boot.order", "grub.map", "disk.map"],
                "correct": 0,
                "explanation": "device.map mapeia dispositivos do GRUB para dispositivos do sistema."
            },
            {
                "question": "Digite o comando para criar entrada de boot UEFI personalizada:",
                "type": "text",
                "correct": ["efibootmgr -c"],
                "explanation": "efibootmgr -c cria nova entrada de boot UEFI."
            },
        ]
    
    def _get_102_3_questions(self):
        """Gerenciamento de Bibliotecas Compartilhadas (102.3)"""
        return [
            {
                "question": "Qual comando lista bibliotecas compartilhadas usadas por um executável?",
                "type": "multiple",
                "options": ["ldd", "ldconfig", "liblist", "sharedlibs"],
                "correct": 0,
                "explanation": "ldd mostra dependências de bibliotecas compartilhadas de um binário."
            },
            {
                "question": "Digite o comando para atualizar o cache de bibliotecas:",
                "type": "text",
                "correct": ["ldconfig"],
                "explanation": "ldconfig atualiza cache /etc/ld.so.cache com bibliotecas disponíveis."
            },
            {
                "question": "Onde ficam as configurações de diretórios de bibliotecas?",
                "type": "multiple",
                "options": ["/etc/ld.so.conf", "/etc/libs.conf", "/etc/library.conf", "/lib/ld.conf"],
                "correct": 0,
                "explanation": "/etc/ld.so.conf define diretórios onde o sistema procura bibliotecas."
            },
            {
                "question": "Digite o diretório padrão para bibliotecas de 64 bits:",
                "type": "text",
                "correct": ["/lib64", "/usr/lib64", "/lib/x86_64-linux-gnu"],
                "explanation": "/lib64 e /usr/lib64 (ou /lib/x86_64-linux-gnu no Debian) para libs 64-bit."
            },
            {
                "question": "Qual variável de ambiente sobrescreve o caminho de bibliotecas?",
                "type": "multiple",
                "options": ["LD_LIBRARY_PATH", "LIBRARY_PATH", "LIB_PATH", "SHARED_LIB_PATH"],
                "correct": 0,
                "explanation": "LD_LIBRARY_PATH define diretórios adicionais para busca de bibliotecas."
            },
            {
                "question": "Em qual diretório adicional ld.so.conf busca arquivos .conf?",
                "type": "multiple",
                "options": ["/etc/ld.so.conf.d/", "/etc/lib.conf.d/", "/usr/lib/ld.conf.d/", "/var/ld.conf.d/"],
                "correct": 0,
                "explanation": "/etc/ld.so.conf.d/*.conf contém configurações adicionais de bibliotecas."
            },
            {
                "question": "Digite o arquivo de cache de bibliotecas gerado pelo ldconfig:",
                "type": "text",
                "correct": ["/etc/ld.so.cache"],
                "explanation": "/etc/ld.so.cache é cache binário de bibliotecas disponíveis."
            },
            {
                "question": "Qual opção do ldconfig mostra as bibliotecas no cache?",
                "type": "multiple",
                "options": ["ldconfig -p", "ldconfig -l", "ldconfig -s", "ldconfig -v"],
                "correct": 0,
                "explanation": "ldconfig -p imprime bibliotecas atualmente no cache."
            },
            {
                "question": "Onde ficam bibliotecas de 32 bits em sistemas 64 bits?",
                "type": "multiple",
                "options": ["/lib32 ou /usr/lib32", "/lib/i386", "/usr/lib/32", "/lib64/compat"],
                "correct": 0,
                "explanation": "/lib32 e /usr/lib32 contêm bibliotecas 32-bit em sistemas 64-bit."
            },
            {
                "question": "Digite o comando para ver versão de uma biblioteca:",
                "type": "text",
                "correct": ["ldd", "strings", "objdump"],
                "explanation": "strings <lib> | grep VERSION ou objdump podem mostrar versão."
            },
            {
                "question": "Qual prefixo de nome indica biblioteca compartilhada Linux?",
                "type": "multiple",
                "options": ["lib*.so*", "shared*.so", "*.dll", "*.dylib"],
                "correct": 0,
                "explanation": "Bibliotecas compartilhadas Linux seguem padrão lib<nome>.so.<versão>."
            },
            {
                "question": "Em RedHat, qual diretório contém bibliotecas do sistema?",
                "type": "multiple",
                "options": ["/usr/lib64", "/lib", "/usr/local/lib", "/opt/lib"],
                "correct": 0,
                "explanation": "RedHat 64-bit usa /usr/lib64 para bibliotecas do sistema."
            },
            {
                "question": "Digite o comando para verificar qual biblioteca um símbolo pertence:",
                "type": "text",
                "correct": ["nm", "objdump"],
                "explanation": "nm -D <lib> lista símbolos de bibliotecas compartilhadas."
            },
            {
                "question": "Qual variável força carregamento de biblioteca específica?",
                "type": "multiple",
                "options": ["LD_PRELOAD", "LD_LOAD", "LIB_PRELOAD", "PRELOAD_LIB"],
                "correct": 0,
                "explanation": "LD_PRELOAD força carregamento de bibliotecas específicas antes de outras."
            },
            {
                "question": "Onde OpenSUSE armazena bibliotecas do sistema?",
                "type": "multiple",
                "options": ["/usr/lib64", "/lib64", "/usr/lib", "Todas as anteriores"],
                "correct": 3,
                "explanation": "OpenSUSE usa /lib64, /usr/lib64 para 64-bit e /lib, /usr/lib para 32-bit."
            },
            {
                "question": "Digite o tipo MIME de bibliotecas compartilhadas ELF:",
                "type": "text",
                "correct": ["application/x-sharedlib", "ELF"],
                "explanation": "Bibliotecas compartilhadas são arquivos ELF (Executable and Linkable Format)."
            },
            {
                "question": "Qual comando mostra cabeçalho ELF de uma biblioteca?",
                "type": "multiple",
                "options": ["readelf -h", "file", "elfinfo", "libheader"],
                "correct": 0,
                "explanation": "readelf -h exibe cabeçalho ELF com informações da biblioteca."
            },
            {
                "question": "Em Debian, onde ficam bibliotecas específicas da arquitetura?",
                "type": "multiple",
                "options": ["/usr/lib/x86_64-linux-gnu", "/lib64", "/usr/lib64", "/lib/amd64"],
                "correct": 0,
                "explanation": "Debian usa /usr/lib/x86_64-linux-gnu para multiarch."
            },
            {
                "question": "Digite o comando para listar símbolos dinâmicos de uma biblioteca:",
                "type": "text",
                "correct": ["nm -D", "objdump -T"],
                "explanation": "nm -D ou objdump -T listam símbolos dinâmicos exportados."
            },
            {
                "question": "Qual arquivo define bibliotecas confiáveis para SUID?",
                "type": "multiple",
                "options": ["/etc/ld.so.preload", "/etc/ld.so.trusted", "/etc/lib.trusted", "/etc/secure.libs"],
                "correct": 0,
                "explanation": "/etc/ld.so.preload lista bibliotecas carregadas para todos os programas."
            },
            {
                "question": "Digite a opção do ldd para mostrar funções não utilizadas:",
                "type": "text",
                "correct": ["ldd -u", "-u"],
                "explanation": "ldd -u mostra objetos compartilhados não utilizados."
            },
            {
                "question": "Qual comando cria links simbólicos para bibliotecas?",
                "type": "multiple",
                "options": ["ldconfig", "ln -s", "liblink", "solink"],
                "correct": 0,
                "explanation": "ldconfig cria links simbólicos necessários para bibliotecas (lib.so -> lib.so.X.Y)."
            },
            {
                "question": "Em qual diretório ficam bibliotecas instaladas localmente?",
                "type": "multiple",
                "options": ["/usr/local/lib", "/opt/lib", "/home/lib", "/var/lib"],
                "correct": 0,
                "explanation": "/usr/local/lib é para bibliotecas instaladas manualmente/localmente."
            },
            {
                "question": "Digite o sufixo de número de versão em bibliotecas compartilhadas:",
                "type": "text",
                "correct": [".so", "so"],
                "explanation": "Bibliotecas usam .so.MAJOR.MINOR.PATCH (ex: libtest.so.1.2.3)."
            },
            {
                "question": "Qual variável define loader dinâmico alternativo?",
                "type": "multiple",
                "options": ["LD_LOADER", "LD_DYNAMIC_LOADER", "Nenhuma - se usa /lib/ld-linux.so", "LOADER_PATH"],
                "correct": 2,
                "explanation": "O loader é /lib/ld-linux.so.2 (32-bit) ou /lib64/ld-linux-x86-64.so.2 (64-bit), não configurável por variável."
            },
        ]
    
    def _get_102_4_questions(self):
        """Gerenciamento de Pacotes Debian (102.4)"""
        return [
            {
                "question": "Qual comando instala um pacote .deb?",
                "type": "multiple",
                "options": ["dpkg -i", "apt install", "dpkg install", "apt -i"],
                "correct": 0,
                "explanation": "dpkg -i instala pacote .deb local. apt install busca de repositórios."
            },
            {
                "question": "Digite o comando para atualizar lista de pacotes disponíveis:",
                "type": "text",
                "correct": ["apt update", "apt-get update"],
                "explanation": "apt update ou apt-get update atualiza lista de pacotes dos repositórios."
            },
            {
                "question": "Qual comando atualiza todos os pacotes instalados?",
                "type": "multiple",
                "options": ["apt upgrade", "apt update", "dpkg --upgrade", "apt-get dist-upgrade"],
                "correct": 0,
                "explanation": "apt upgrade atualiza pacotes. dist-upgrade atualiza com mudanças de dependências."
            },
            {
                "question": "Digite o comando para remover pacote mantendo arquivos de configuração:",
                "type": "text",
                "correct": ["apt remove", "dpkg -r"],
                "explanation": "apt remove ou dpkg -r removem pacote mas mantêm configurações."
            },
            {
                "question": "Qual comando remove pacote incluindo configurações?",
                "type": "multiple",
                "options": ["apt purge", "apt remove --purge", "dpkg -P", "Todas as anteriores"],
                "correct": 3,
                "explanation": "apt purge, apt remove --purge ou dpkg -P removem pacote e configurações."
            },
            {
                "question": "Onde ficam os repositórios APT no Debian/Ubuntu?",
                "type": "multiple",
                "options": ["/etc/apt/sources.list", "/etc/apt/repos", "/etc/sources.list", "/var/apt/sources"],
                "correct": 0,
                "explanation": "/etc/apt/sources.list e /etc/apt/sources.list.d/*.list definem repositórios."
            },
            {
                "question": "Digite o comando para buscar um pacote nos repositórios:",
                "type": "text",
                "correct": ["apt search", "apt-cache search"],
                "explanation": "apt search ou apt-cache search buscam pacotes por nome/descrição."
            },
            {
                "question": "Qual comando mostra informações detalhadas de um pacote?",
                "type": "multiple",
                "options": ["apt show", "apt-cache show", "dpkg -s", "Todas as anteriores"],
                "correct": 3,
                "explanation": "apt show, apt-cache show mostram info de repositório. dpkg -s de instalados."
            },
            {
                "question": "Digite o comando para listar arquivos de um pacote instalado:",
                "type": "text",
                "correct": ["dpkg -L", "dpkg --listfiles"],
                "explanation": "dpkg -L <pacote> lista todos os arquivos instalados pelo pacote."
            },
            {
                "question": "Qual comando identifica a qual pacote um arquivo pertence?",
                "type": "multiple",
                "options": ["dpkg -S", "apt-file search", "dpkg-query -S", "a e c"],
                "correct": 3,
                "explanation": "dpkg -S <arquivo> ou dpkg-query -S mostra qual pacote instalou o arquivo."
            },
            {
                "question": "Digite o diretório onde APT armazena pacotes baixados:",
                "type": "text",
                "correct": ["/var/cache/apt/archives"],
                "explanation": "/var/cache/apt/archives/ armazena arquivos .deb baixados."
            },
            {
                "question": "Qual comando limpa cache de pacotes antigos?",
                "type": "multiple",
                "options": ["apt clean", "apt autoclean", "apt-get clean", "Todas as anteriores"],
                "correct": 3,
                "explanation": "apt clean remove todos .deb. autoclean remove apenas obsoletos."
            },
            {
                "question": "Digite o comando para remover pacotes órfãos (não mais necessários):",
                "type": "text",
                "correct": ["apt autoremove", "apt-get autoremove"],
                "explanation": "apt autoremove remove dependências que não são mais necessárias."
            },
            {
                "question": "Qual comando lista todos os pacotes instalados?",
                "type": "multiple",
                "options": ["dpkg -l", "apt list --installed", "dpkg --list", "Todas as anteriores"],
                "correct": 3,
                "explanation": "dpkg -l ou apt list --installed listam pacotes instalados."
            },
            {
                "question": "Digite o comando para reconfigurar um pacote já instalado:",
                "type": "text",
                "correct": ["dpkg-reconfigure"],
                "explanation": "dpkg-reconfigure <pacote> executa novamente o script de configuração."
            },
            {
                "question": "Qual comando corrige dependências quebradas?",
                "type": "multiple",
                "options": ["apt -f install", "apt --fix-broken install", "dpkg --configure -a", "a e c"],
                "correct": 3,
                "explanation": "apt -f install corrige dependências. dpkg --configure -a configura pacotes pendentes."
            },
            {
                "question": "Onde ficam os scripts de pré/pós instalação de um pacote?",
                "type": "multiple",
                "options": ["/var/lib/dpkg/info/", "/etc/dpkg/", "/usr/share/dpkg/", "/var/cache/dpkg/"],
                "correct": 0,
                "explanation": "/var/lib/dpkg/info/ contém scripts .preinst, .postinst, .prerm, .postrm."
            },
            {
                "question": "Digite o arquivo que registra status de todos os pacotes:",
                "type": "text",
                "correct": ["/var/lib/dpkg/status"],
                "explanation": "/var/lib/dpkg/status contém estado e informações de todos os pacotes."
            },
            {
                "question": "Qual comando bloqueia versão de um pacote (hold)?",
                "type": "multiple",
                "options": ["apt-mark hold", "dpkg --set-selections", "apt hold", "dpkg-hold"],
                "correct": 0,
                "explanation": "apt-mark hold <pacote> impede que o pacote seja atualizado."
            },
            {
                "question": "Digite o comando para extrair arquivos de um .deb sem instalar:",
                "type": "text",
                "correct": ["dpkg -x", "dpkg --extract"],
                "explanation": "dpkg -x <arquivo.deb> <dir> extrai arquivos sem instalar."
            },
            {
                "question": "Qual ferramenta baixa código-fonte de um pacote?",
                "type": "multiple",
                "options": ["apt source", "apt-get source", "Ambas", "dpkg-source"],
                "correct": 2,
                "explanation": "apt source ou apt-get source baixam código-fonte de pacotes."
            },
            {
                "question": "Digite a linha sources.list para adicionar repositório universe do Ubuntu:",
                "type": "text",
                "correct": ["deb http://archive.ubuntu.com/ubuntu jammy universe", "universe"],
                "explanation": "Adicionar 'universe' aos componentes ou linha completa com 'universe'."
            },
            {
                "question": "Qual comando verifica integridade de pacotes instalados?",
                "type": "multiple",
                "options": ["dpkg --verify", "dpkg -V", "debsums", "b e c"],
                "correct": 3,
                "explanation": "dpkg -V ou debsums verificam checksums dos arquivos instalados."
            },
            {
                "question": "Digite o comando para instalar múltiplos pacotes de uma vez:",
                "type": "text",
                "correct": ["apt install pacote1 pacote2 pacote3"],
                "explanation": "apt install aceita múltiplos nomes de pacotes separados por espaço."
            },
            {
                "question": "Qual comando mostra histórico de instalações do apt?",
                "type": "multiple",
                "options": ["cat /var/log/apt/history.log", "apt history", "dpkg.log", "apt log"],
                "correct": 0,
                "explanation": "/var/log/apt/history.log contém histórico de comandos apt."
            },
            {
                "question": "Digite o comando para simular instalação sem executá-la:",
                "type": "text",
                "correct": ["apt install -s", "apt-get -s install"],
                "explanation": "apt install -s (simulate) ou --dry-run mostra o que seria feito."
            },
        ]
    
    def _get_102_5_questions(self):
        """Gerenciamento de Pacotes RPM e YUM (102.5)"""
        return [
            {
                "question": "Qual comando instala um pacote RPM local?",
                "type": "multiple",
                "options": ["rpm -i", "yum localinstall", "rpm install", "dnf -i"],
                "correct": 0,
                "explanation": "rpm -i ou -ivh instala pacote RPM local sem resolver dependências."
            },
            {
                "question": "Digite o comando YUM para instalar um pacote dos repositórios:",
                "type": "text",
                "correct": ["yum install", "dnf install"],
                "explanation": "yum install (CentOS 7) ou dnf install (CentOS 8+, Fedora) instala pacotes."
            },
            {
                "question": "Qual comando atualiza todos os pacotes no RedHat/CentOS?",
                "type": "multiple",
                "options": ["yum update", "dnf update", "yum upgrade", "Todas as anteriores"],
                "correct": 3,
                "explanation": "yum/dnf update ou upgrade atualizam todos os pacotes do sistema."
            },
            {
                "question": "Digite o comando para remover pacote com YUM:",
                "type": "text",
                "correct": ["yum remove", "yum erase"],
                "explanation": "yum remove ou yum erase removem pacote e suas dependências não utilizadas."
            },
            {
                "question": "Qual comando lista todos os pacotes instalados com RPM?",
                "type": "multiple",
                "options": ["rpm -qa", "rpm -q --all", "rpm --list", "a e b"],
                "correct": 3,
                "explanation": "rpm -qa ou rpm -q --all listam todos os pacotes instalados."
            },
            {
                "question": "Onde ficam os repositórios YUM no CentOS/RedHat?",
                "type": "multiple",
                "options": ["/etc/yum.repos.d/", "/etc/yum.conf.d/", "/var/yum/repos/", "/etc/repos.d/"],
                "correct": 0,
                "explanation": "/etc/yum.repos.d/*.repo contém definições de repositórios YUM."
            },
            {
                "question": "Digite o comando para buscar pacote nos repositórios YUM:",
                "type": "text",
                "correct": ["yum search", "dnf search"],
                "explanation": "yum search ou dnf search buscam pacotes por nome e descrição."
            },
            {
                "question": "Qual comando mostra informações de um pacote com RPM?",
                "type": "multiple",
                "options": ["rpm -qi", "rpm --info", "rpm -q --info", "a e c"],
                "correct": 3,
                "explanation": "rpm -qi <pacote> mostra informações detalhadas de pacote instalado."
            },
            {
                "question": "Digite o comando para listar arquivos de um pacote RPM:",
                "type": "text",
                "correct": ["rpm -ql", "rpm -q --list"],
                "explanation": "rpm -ql <pacote> lista arquivos instalados por um pacote."
            },
            {
                "question": "Qual comando identifica qual pacote RPM fornece um arquivo?",
                "type": "multiple",
                "options": ["rpm -qf", "yum provides", "rpm --whatprovides", "a e b"],
                "correct": 3,
                "explanation": "rpm -qf <arquivo> ou yum provides <arquivo> identificam o pacote."
            },
            {
                "question": "Em OpenSUSE, qual gerenciador de pacotes é usado?",
                "type": "multiple",
                "options": ["zypper", "yum", "apt", "urpmi"],
                "correct": 0,
                "explanation": "OpenSUSE usa zypper como gerenciador de pacotes high-level."
            },
            {
                "question": "Digite o comando zypper para instalar pacote:",
                "type": "text",
                "correct": ["zypper install", "zypper in"],
                "explanation": "zypper install ou zypper in instala pacotes no OpenSUSE."
            },
            {
                "question": "Qual comando atualiza lista de repositórios no zypper?",
                "type": "multiple",
                "options": ["zypper refresh", "zypper update", "zypper ref", "a e c"],
                "correct": 3,
                "explanation": "zypper refresh ou zypper ref atualiza metadados dos repositórios."
            },
            {
                "question": "Digite o comando para remover pacote no OpenSUSE:",
                "type": "text",
                "correct": ["zypper remove", "zypper rm"],
                "explanation": "zypper remove ou zypper rm removem pacotes no OpenSUSE."
            },
            {
                "question": "Qual opção do rpm força instalação ignorando conflitos?",
                "type": "multiple",
                "options": ["--force", "--nodeps", "--ignoreconflicts", "--override"],
                "correct": 0,
                "explanation": "rpm -i --force força instalação mesmo com conflitos (use com cuidado)."
            },
            {
                "question": "Digite o comando para atualizar pacote RPM existente:",
                "type": "text",
                "correct": ["rpm -U", "rpm --upgrade"],
                "explanation": "rpm -U ou --upgrade atualiza pacote instalado ou instala se não existir."
            },
            {
                "question": "Qual comando remove pacote RPM sem verificar dependências?",
                "type": "multiple",
                "options": ["rpm -e --nodeps", "rpm -r", "rpm remove", "rpm erase"],
                "correct": 0,
                "explanation": "rpm -e --nodeps remove pacote sem verificar se outros dependem dele."
            },
            {
                "question": "Onde YUM armazena cache de pacotes baixados?",
                "type": "multiple",
                "options": ["/var/cache/yum/", "/var/yum/cache/", "/tmp/yum/", "/var/lib/yum/"],
                "correct": 0,
                "explanation": "/var/cache/yum/ armazena metadados e pacotes baixados pelo YUM."
            },
            {
                "question": "Digite o comando para limpar cache do YUM:",
                "type": "text",
                "correct": ["yum clean all", "dnf clean all"],
                "explanation": "yum clean all ou dnf clean all limpam todo o cache."
            },
            {
                "question": "Qual comando lista repositórios habilitados no YUM?",
                "type": "multiple",
                "options": ["yum repolist", "dnf repolist", "yum repo list", "a e b"],
                "correct": 3,
                "explanation": "yum repolist ou dnf repolist listam repositórios ativos."
            },
            {
                "question": "Digite o comando para verificar atualizações disponíveis sem instalar:",
                "type": "text",
                "correct": ["yum check-update", "dnf check-update"],
                "explanation": "yum check-update lista pacotes com atualizações disponíveis."
            },
            {
                "question": "Qual comando mostra histórico de transações do YUM?",
                "type": "multiple",
                "options": ["yum history", "dnf history", "yum log", "a e b"],
                "correct": 3,
                "explanation": "yum history ou dnf history mostram histórico de instalações/remoções."
            },
            {
                "question": "Digite o comando para desfazer última transação YUM:",
                "type": "text",
                "correct": ["yum history undo", "dnf history undo"],
                "explanation": "yum history undo <ID> reverte transação específica."
            },
            {
                "question": "Em OpenSUSE, onde ficam os repositórios do zypper?",
                "type": "multiple",
                "options": ["/etc/zypp/repos.d/", "/etc/zypper/repos/", "/var/zypp/repos/", "/etc/repos.d/"],
                "correct": 0,
                "explanation": "/etc/zypp/repos.d/ contém arquivos .repo do zypper."
            },
            {
                "question": "Qual comando adiciona repositório no zypper?",
                "type": "multiple",
                "options": ["zypper addrepo", "zypper ar", "zypper repo add", "a e b"],
                "correct": 3,
                "explanation": "zypper addrepo ou zypper ar adicionam novo repositório."
            },
        ]
    
    def _get_103_1_questions(self):
        """Linha de Comando (103.1)"""
        return [
            {
                "question": "Qual variável de ambiente contém o PATH de comandos?",
                "type": "multiple",
                "options": ["PATH", "COMMAND_PATH", "BIN_PATH", "EXEC_PATH"],
                "correct": 0,
                "explanation": "PATH define diretórios onde o shell busca comandos executáveis."
            },
            {
                "question": "Digite o comando para ver o valor de uma variável de ambiente:",
                "type": "text",
                "correct": ["echo $VARIAVEL", "printenv", "env"],
                "explanation": "echo $VAR mostra valor. printenv ou env listam todas as variáveis."
            },
            {
                "question": "Qual comando define variável de ambiente para sessão atual?",
                "type": "multiple",
                "options": ["export VAR=valor", "set VAR=valor", "env VAR=valor", "setenv VAR valor"],
                "correct": 0,
                "explanation": "export VAR=valor define variável de ambiente no bash."
            },
            {
                "question": "Digite o arquivo que carrega variáveis para todos os usuários no login:",
                "type": "text",
                "correct": ["/etc/profile", "/etc/environment"],
                "explanation": "/etc/profile (bash) ou /etc/environment (PAM) são carregados para todos."
            },
            {
                "question": "Qual arquivo pessoal é carregado no login bash interativo?",
                "type": "multiple",
                "options": ["~/.bash_profile ou ~/.profile", "~/.bashrc", "~/.bash_login", "Todas as anteriores"],
                "correct": 3,
                "explanation": "bash procura ~/.bash_profile, ~/.bash_login, ~/.profile nesta ordem."
            },
            {
                "question": "Digite o arquivo carregado em shells bash não-login:",
                "type": "text",
                "correct": ["~/.bashrc"],
                "explanation": "~/.bashrc é executado para shells interativos não-login."
            },
            {
                "question": "Qual comando executa script no contexto do shell atual?",
                "type": "multiple",
                "options": ["source", ".", "exec", "a e b"],
                "correct": 3,
                "explanation": "source <arquivo> ou . <arquivo> executam no shell atual."
            },
            {
                "question": "Digite o comando para ver o shell atual do usuário:",
                "type": "text",
                "correct": ["echo $SHELL", "echo $0"],
                "explanation": "echo $SHELL mostra shell padrão. echo $0 mostra shell atual."
            },
            {
                "question": "Qual variável contém o diretório home do usuário?",
                "type": "multiple",
                "options": ["HOME", "HOMEDIR", "USER_HOME", "HOME_PATH"],
                "correct": 0,
                "explanation": "$HOME contém o caminho do diretório home do usuário."
            },
            {
                "question": "Digite o comando para listar aliases definidos:",
                "type": "text",
                "correct": ["alias"],
                "explanation": "alias sem argumentos lista todos os aliases configurados."
            },
            {
                "question": "Qual comando cria um alias temporário?",
                "type": "multiple",
                "options": ["alias nome='comando'", "set alias", "export alias", "newalias"],
                "correct": 0,
                "explanation": "alias nome='comando' cria alias para sessão atual."
            },
            {
                "question": "Digite o comando para remover um alias:",
                "type": "text",
                "correct": ["unalias"],
                "explanation": "unalias <nome> remove alias definido."
            },
            {
                "question": "Qual comando mostra o tipo/localização de um comando?",
                "type": "multiple",
                "options": ["type", "which", "whereis", "Todas as anteriores"],
                "correct": 3,
                "explanation": "type, which e whereis mostram informações sobre comandos/arquivos."
            },
            {
                "question": "Digite o símbolo para executar comando em background:",
                "type": "text",
                "correct": ["&"],
                "explanation": "& no final do comando executa em background."
            },
            {
                "question": "Qual comando lista jobs em execução no shell atual?",
                "type": "multiple",
                "options": ["jobs", "ps", "bg", "fg"],
                "correct": 0,
                "explanation": "jobs lista processos iniciados pelo shell atual."
            },
            {
                "question": "Digite o comando para trazer job para foreground:",
                "type": "text",
                "correct": ["fg"],
                "explanation": "fg %numero traz job para foreground."
            },
            {
                "question": "Qual comando continua job pausado em background?",
                "type": "multiple",
                "options": ["bg", "fg", "continue", "resume"],
                "correct": 0,
                "explanation": "bg %numero continua job pausado em background."
            },
            {
                "question": "Digite a combinação de teclas para pausar processo em foreground:",
                "type": "text",
                "correct": ["Ctrl+Z", "^Z"],
                "explanation": "Ctrl+Z (^Z) envia SIGTSTP, pausando processo em foreground."
            },
            {
                "question": "Qual variável contém o código de saída do último comando?",
                "type": "multiple",
                "options": ["$?", "$!", "$#", "$"],
                "correct": 0,
                "explanation": "$? contém exit status do último comando (0 = sucesso)."
            },
            {
                "question": "Digite o comando para ver histórico de comandos:",
                "type": "text",
                "correct": ["history"],
                "explanation": "history lista comandos executados anteriormente."
            },
            {
                "question": "Qual variável define quantos comandos ficam no histórico?",
                "type": "multiple",
                "options": ["HISTSIZE", "HISTFILESIZE", "HISTORY_SIZE", "HIST_MAX"],
                "correct": 0,
                "explanation": "HISTSIZE define número de comandos mantidos em memória."
            },
            {
                "question": "Digite o arquivo que armazena histórico bash permanentemente:",
                "type": "text",
                "correct": ["~/.bash_history"],
                "explanation": "~/.bash_history salva histórico de comandos entre sessões."
            },
            {
                "question": "Qual símbolo repete o último comando no bash?",
                "type": "multiple",
                "options": ["!!", "!$", "!^", "!*"],
                "correct": 0,
                "explanation": "!! repete último comando. !$ repete último argumento."
            },
            {
                "question": "Digite o comando para limpar tela do terminal:",
                "type": "text",
                "correct": ["clear", "Ctrl+L"],
                "explanation": "clear ou Ctrl+L limpam a tela do terminal."
            },
            {
                "question": "Qual comando executa comandos sequencialmente independente de erros?",
                "type": "multiple",
                "options": ["cmd1 ; cmd2", "cmd1 && cmd2", "cmd1 || cmd2", "cmd1 | cmd2"],
                "correct": 0,
                "explanation": "; executa comandos em sequência. && só continua se anterior teve sucesso."
            },
        ]
    
    def _get_103_2_questions(self):
        """Processamento de Texto (103.2)"""
        return [
            {
                "question": "Qual comando exibe conteúdo de arquivo na tela?",
                "type": "multiple",
                "options": ["cat", "more", "less", "Todas as anteriores"],
                "correct": 3,
                "explanation": "cat mostra tudo. more/less permitem navegação por páginas."
            },
            {
                "question": "Digite o comando para mostrar primeiras 10 linhas de arquivo:",
                "type": "text",
                "correct": ["head"],
                "explanation": "head mostra primeiras linhas (padrão 10). head -n 20 para 20 linhas."
            },
            {
                "question": "Qual comando mostra últimas linhas de um arquivo?",
                "type": "multiple",
                "options": ["tail", "end", "last", "bottom"],
                "correct": 0,
                "explanation": "tail mostra últimas linhas. tail -f acompanha arquivo em tempo real."
            },
            {
                "question": "Digite o comando para contar linhas, palavras e caracteres:",
                "type": "text",
                "correct": ["wc"],
                "explanation": "wc conta linhas, palavras e bytes. wc -l conta só linhas."
            },
            {
                "question": "Qual comando ordena linhas de arquivo?",
                "type": "multiple",
                "options": ["sort", "order", "arrange", "rank"],
                "correct": 0,
                "explanation": "sort ordena linhas. sort -r ordem reversa. sort -n ordem numérica."
            },
            {
                "question": "Digite o comando para remover linhas duplicadas consecutivas:",
                "type": "text",
                "correct": ["uniq"],
                "explanation": "uniq remove duplicatas consecutivas. Geralmente usado com sort."
            },
            {
                "question": "Qual comando extrai colunas de texto delimitado?",
                "type": "multiple",
                "options": ["cut", "awk", "column", "a e b"],
                "correct": 3,
                "explanation": "cut -d: -f1 extrai campo. awk é mais poderoso para processar colunas."
            },
            {
                "question": "Digite o comando para substituir caracteres em texto:",
                "type": "text",
                "correct": ["tr"],
                "explanation": "tr 'abc' 'xyz' traduz caracteres. tr -d 'a' deleta caracteres."
            },
            {
                "question": "Qual comando procura padrões em arquivos?",
                "type": "multiple",
                "options": ["grep", "find", "search", "locate"],
                "correct": 0,
                "explanation": "grep procura padrões em conteúdo. find busca arquivos."
            },
            {
                "question": "Digite a opção do grep para busca case-insensitive:",
                "type": "text",
                "correct": ["-i", "--ignore-case"],
                "explanation": "grep -i ignora diferença entre maiúsculas/minúsculas."
            },
            {
                "question": "Qual opção do grep mostra número da linha?",
                "type": "multiple",
                "options": ["-n", "-l", "-c", "-v"],
                "correct": 0,
                "explanation": "grep -n mostra número da linha. -l mostra nome do arquivo. -c conta matches."
            },
            {
                "question": "Digite o comando para busca recursiva em diretórios com grep:",
                "type": "text",
                "correct": ["grep -r", "grep -R"],
                "explanation": "grep -r ou -R busca recursivamente em diretórios."
            },
            {
                "question": "Qual comando edita arquivos com expressões regulares (stream editor)?",
                "type": "multiple",
                "options": ["sed", "awk", "ed", "vi"],
                "correct": 0,
                "explanation": "sed é stream editor para transformações de texto."
            },
            {
                "question": "Digite o comando sed para substituir primeira ocorrência por linha:",
                "type": "text",
                "correct": ["sed 's/old/new/'", "s/old/new/"],
                "explanation": "sed 's/antigo/novo/' substitui primeira ocorrência. 's/old/new/g' todas."
            },
            {
                "question": "Qual comando é linguagem de processamento de padrões?",
                "type": "multiple",
                "options": ["awk", "sed", "perl", "python"],
                "correct": 0,
                "explanation": "awk é linguagem para processamento de texto estruturado em campos."
            },
            {
                "question": "Digite o comando para dividir arquivo em partes:",
                "type": "text",
                "correct": ["split"],
                "explanation": "split divide arquivo. split -l 100 divide a cada 100 linhas."
            },
            {
                "question": "Qual comando junta linhas de arquivos lado a lado?",
                "type": "multiple",
                "options": ["paste", "join", "merge", "combine"],
                "correct": 0,
                "explanation": "paste junta linhas horizontalmente. join junta baseado em campos comuns."
            },
            {
                "question": "Digite o comando para expandir tabs em espaços:",
                "type": "text",
                "correct": ["expand"],
                "explanation": "expand converte tabs em espaços. unexpand faz o inverso."
            },
            {
                "question": "Qual comando formata texto em colunas de largura fixa?",
                "type": "multiple",
                "options": ["fmt", "fold", "column", "pr"],
                "correct": 0,
                "explanation": "fmt formata parágrafos. fold quebra linhas em largura específica."
            },
            {
                "question": "Digite o comando para numerar linhas de arquivo:",
                "type": "text",
                "correct": ["nl", "cat -n"],
                "explanation": "nl numera linhas. cat -n também adiciona números de linha."
            },
            {
                "question": "Qual opção do sort ordena numericamente?",
                "type": "multiple",
                "options": ["-n", "-g", "-h", "-r"],
                "correct": 0,
                "explanation": "sort -n ordem numérica. -g ordem numérica geral. -h human-readable."
            },
            {
                "question": "Digite o comando para ver diferenças entre dois arquivos:",
                "type": "text",
                "correct": ["diff"],
                "explanation": "diff compara arquivos linha a linha mostrando diferenças."
            },
            {
                "question": "Qual comando cria checksum MD5 de arquivo?",
                "type": "multiple",
                "options": ["md5sum", "md5", "checksum", "hash"],
                "correct": 0,
                "explanation": "md5sum gera hash MD5. sha256sum para SHA-256."
            },
            {
                "question": "Digite o comando para converter e copiar arquivos:",
                "type": "text",
                "correct": ["dd"],
                "explanation": "dd copia/converte arquivos. Usado para criar imagens de disco, etc."
            },
            {
                "question": "Qual comando mostra tipo/encoding de arquivo?",
                "type": "multiple",
                "options": ["file", "type", "filetype", "encoding"],
                "correct": 0,
                "explanation": "file determina tipo de arquivo examinando seu conteúdo."
            },
        ]
    
    def _get_103_3_questions(self):
        """Gerenciamento de Processos (103.3)"""
        return [
            {
                "question": "Qual comando lista processos em execução?",
                "type": "multiple",
                "options": ["ps", "top", "pstree", "Todas as anteriores"],
                "correct": 3,
                "explanation": "ps lista processos. top mostra em tempo real. pstree em árvore."
            },
            {
                "question": "Digite o comando para ver todos os processos do sistema:",
                "type": "text",
                "correct": ["ps aux", "ps -ef"],
                "explanation": "ps aux (BSD) ou ps -ef (Unix) mostram todos os processos."
            },
            {
                "question": "Qual comando mostra processos em formato de árvore?",
                "type": "multiple",
                "options": ["pstree", "ps --forest", "ps -ejH", "Todas as anteriores"],
                "correct": 3,
                "explanation": "pstree, ps --forest ou ps -ejH mostram hierarquia de processos."
            },
            {
                "question": "Digite o comando interativo para monitorar processos:",
                "type": "text",
                "correct": ["top", "htop"],
                "explanation": "top monitora processos. htop é versão mais amigável (se instalado)."
            },
            {
                "question": "Qual sinal termina processo normalmente?",
                "type": "multiple",
                "options": ["SIGTERM (15)", "SIGKILL (9)", "SIGHUP (1)", "SIGINT (2)"],
                "correct": 0,
                "explanation": "SIGTERM (15) permite que processo finalize graciosamente."
            },
            
            {
                "question": "Digite o comando para enviar sinal a um processo:",
                "type": "text",
                "correct": ["kill"],
                "explanation": "kill <PID> envia SIGTERM. kill -9 <PID> força término (SIGKILL)."
            },

            {
                "question": "Qual comando mata processo por nome?",
                "type": "multiple",
                "options": ["pkill", "killall", "kill -n", "a e b"],
                "correct": 3,
                "explanation": "pkill <nome> ou killall <nome> terminam processos pelo nome."
            },
            {
                "question": "Digite o comando para ver sinais disponíveis para kill:",
                "type": "text",
                "correct": ["kill -l"],
                "explanation": "kill -l lista todos os sinais disponíveis."
            },
            {
                "question": "Qual comando mostra uso de CPU e memória em tempo real?",
                "type": "multiple",
                "options": ["top", "vmstat", "free", "a e b"],
                "correct": 3,
                "explanation": "top interativo. vmstat mostra estatísticas do sistema."
            },
            {
                "question": "Digite o comando para alterar prioridade (nice) de processo existente:",
                "type": "text",
                "correct": ["renice"],
                "explanation": "renice altera prioridade de processo rodando. nice define para novo."
            },
            {
                "question": "Qual valor nice tem maior prioridade?",
                "type": "multiple",
                "options": ["-20", "0", "19", "100"],
                "correct": 0,
                "explanation": "nice -20 é maior prioridade. nice 19 é menor prioridade."
            },
            {
                "question": "Digite o comando para ver consumo de memória de processos:",
                "type": "text",
                "correct": ["ps aux --sort -rss", "top"],
                "explanation": "ps aux --sort -rss ordena por memória. top mostra em tempo real."
            },
            {
                "question": "Qual variável mostra PID do shell atual?",
                "type": "multiple",
                "options": ["$$", "$PPID", "$!", "$?"],
                "correct": 0,
                "explanation": "$$ contém PID do processo shell atual."
            },
            {
                "question": "Digite o comando para ver processos filhos de um PID:",
                "type": "text",
                "correct": ["ps --ppid", "pstree -p"],
                "explanation": "ps --ppid <PID> mostra filhos diretos. pstree -p mostra árvore completa."
            },
            {
                "question": "Qual arquivo contém informações de processos em execução?",
                "type": "multiple",
                "options": ["/proc/[pid]/", "/var/run/", "/tmp/", "/dev/shm/"],
                "correct": 0,
                "explanation": "/proc/[pid]/ contém diretórios virtuais para cada processo."
            },
            {
                "question": "Digite o comando para ver arquivos abertos por processo:",
                "type": "text",
                "correct": ["lsof"],
                "explanation": "lsof lista arquivos abertos por processos. lsof -p <PID> para processo específico."
            },
            {
                "question": "Qual comando mostra uso de recursos por processo?",
                "type": "multiple",
                "options": ["pidstat", "sar", "vmstat", "Todas as anteriores"],
                "correct": 0,
                "explanation": "pidstat mostra estatísticas de uso de CPU/memória por processo."
            },
            {
                "question": "Digite o comando para ver rede de processo:",
                "type": "text",
                "correct": ["netstat -tulpn", "ss -tulpn"],
                "explanation": "netstat -tulpn ou ss -tulpn mostram conexões com PIDs."
            },
            {
                "question": "Qual comando termina processos de usuário específico?",
                "type": "multiple",
                "options": ["pkill -u", "killall -u", "kill -u", "a e b"],
                "correct": 3,
                "explanation": "pkill -u <user> ou killall -u <user> terminam processos do usuário."
            },
            {
                "question": "Digite o comando para ver threads de processo:",
                "type": "text",
                "correct": ["ps -L", "top -H"],
                "explanation": "ps -L <PID> mostra threads. top com H alterna para modo threads."
            },
            {
                "question": "Qual opção do ps mostra threads?",
                "type": "multiple",
                "options": ["ps -eLf", "ps -T", "ps -mt", "a e b"],
                "correct": 3,
                "explanation": "ps -eLf ou ps -T mostram informações de threads."
            },
            {
                "question": "Digite o comando para ver últimos processos que terminaram:",
                "type": "text",
                "correct": ["lastcomm", "sa"],
                "explanation": "lastcomm mostra histórico de comandos. sa resume informações."
            },
            {
                "question": "Qual comando mostra consumo de recursos por usuário?",
                "type": "multiple",
                "options": ["ps aux --sort user", "top -u", "a e b", "Nenhum"],
                "correct": 2,
                "explanation": "ps aux --sort user ou top -u <usuario> mostram por usuário."
            },
            {
                "question": "Digite o comando para criar snapshot atual de processos:",
                "type": "text",
                "correct": ["ps aux > processos.txt"],
                "explanation": "Redirecionar saída do ps para arquivo cria snapshot para análise."
            },
        ]
    
    def _get_103_4_questions(self):
        """Utilidades de Busca (103.4)"""
        return [
            {
                "question": "Qual comando busca arquivos por nome?",
                "type": "multiple",
                "options": ["find", "locate", "which", "Todas as anteriores"],
                "correct": 3,
                "explanation": "find busca por critérios. locate usa banco de dados. which mostra caminho de executáveis."
            },
            {
                "question": "Digite o comando find para buscar arquivos por nome:",
                "type": "text",
                "correct": ["find / -name 'arquivo'"],
                "explanation": "find / -name 'nome' busca arquivos com nome específico a partir da raiz."
            },
            {
                "question": "Qual comando usa banco de dados para busca mais rápida?",
                "type": "multiple",
                "options": ["locate", "find", "whereis", "search"],
                "correct": 0,
                "explanation": "locate usa banco de dados updatedb. Mais rápido mas pode estar desatualizado."
            },
            {
                "question": "Digite o comando para atualizar banco de dados do locate:",
                "type": "text",
                "correct": ["updatedb"],
                "explanation": "updatedb atualiza banco de dados usado pelo locate. Normalmente rodado via cron."
            },
            {
                "question": "Qual comando busca executáveis no PATH?",
                "type": "multiple",
                "options": ["which", "whereis", "type", "Todas as anteriores"],
                "correct": 3,
                "explanation": "which mostra caminho completo do executável. whereis também mostra manpages."
            },
            {
                "question": "Digite a opção do find para buscar arquivos modificados últimos 7 dias:",
                "type": "text",
                "correct": ["-mtime -7"],
                "explanation": "find / -mtime -7 encontra arquivos modificados nos últimos 7 dias."
            },
            {
                "question": "Qual opção do find executa comando nos arquivos encontrados?",
                "type": "multiple",
                "options": ["-exec", "-xargs", "-run", "-do"],
                "correct": 0,
                "explanation": "find / -name '*.txt' -exec rm {} \\; executa rm para cada arquivo."
            },
            {
                "question": "Digite o comando para buscar arquivos por dono:",
                "type": "text",
                "correct": ["find / -user usuario"],
                "explanation": "find / -user <usuario> busca arquivos pertencentes ao usuário."
            },
            {
                "question": "Qual opção do find busca por tipo (arquivo, diretório)?",
                "type": "multiple",
                "options": ["-type", "-name", "-perm", "-size"],
                "correct": 0,
                "explanation": "find / -type f para arquivos. -type d para diretórios."
            },
            {
                "question": "Digite o comando para buscar arquivos por permissão:",
                "type": "text",
                "correct": ["find / -perm 644"],
                "explanation": "find / -perm 644 encontra arquivos com permissões exatas."
            },
            {
                "question": "Qual comando mostra localização de manpages e arquivos fonte?",
                "type": "multiple",
                "options": ["whereis", "whatis", "apropos", "manpath"],
                "correct": 0,
                "explanation": "whereis mostra binário, source e manpage de programa."
            },
            {
                "question": "Digite o comando para buscar por descrição em manpages:",
                "type": "text",
                "correct": ["apropos", "man -k"],
                "explanation": "apropos <palavra> ou man -k <palavra> buscam nas descrições das manpages."
            },
            {
                "question": "Qual opção do find busca arquivos por tamanho?",
                "type": "multiple",
                "options": ["-size", "-bytes", "-length", "-capacity"],
                "correct": 0,
                "explanation": "find / -size +100M encontra arquivos maiores que 100MB."
            },
            {
                "question": "Digite o comando para buscar arquivos vazios:",
                "type": "text",
                "correct": ["find / -empty"],
                "explanation": "find / -empty encontra arquivos ou diretórios vazios."
            },
            {
                "question": "Qual comando busca texto dentro de arquivos?",
                "type": "multiple",
                "options": ["grep", "find -exec grep", "rgrep", "Todas as anteriores"],
                "correct": 3,
                "explanation": "grep busca conteúdo. find com exec grep busca em arquivos específicos."
            },
            {
                "question": "Digite o comando grep para busca recursiva em diretório atual:",
                "type": "text",
                "correct": ["grep -r 'texto' ."],
                "explanation": "grep -r 'texto' . busca recursivamente do diretório atual."
            },
            {
                "question": "Qual arquivo de configuração do locate armazena diretórios excluídos?",
                "type": "multiple",
                "options": ["/etc/updatedb.conf", "/etc/locate.conf", "/etc/locate.rc", "/var/lib/locate.db"],
                "correct": 0,
                "explanation": "/etc/updatedb.conf define diretórios excluídos do banco locate."
            },
            {
                "question": "Digite a opção do find para limitar profundidade da busca:",
                "type": "text",
                "correct": ["-maxdepth"],
                "explanation": "find / -maxdepth 2 busca apenas até 2 níveis de profundidade."
            },
            {
                "question": "Qual comando combina find com xargs para performance?",
                "type": "multiple",
                "options": ["find / -name '*.tmp' | xargs rm", "find -exec rm", "Ambas", "Nenhuma"],
                "correct": 2,
                "explanation": "xargs é mais eficiente que -exec para muitos arquivos."
            },
            {
                "question": "Digite o comando para buscar arquivos por grupo:",
                "type": "text",
                "correct": ["find / -group grupo"],
                "explanation": "find / -group <grupo> busca arquivos pertencentes ao grupo."
            },
            {
                "question": "Qual comando mostra caminhos onde o sistema busca manpages?",
                "type": "multiple",
                "options": ["manpath", "man --path", "echo $MANPATH", "Todas as anteriores"],
                "correct": 3,
                "explanation": "manpath mostra diretórios de manpages configurados."
            },
            {
                "question": "Digite a opção do find para arquivos acessados recentemente:",
                "type": "text",
                "correct": ["-atime"],
                "explanation": "find / -atime -1 encontra arquivos acessados no último dia."
            },
            {
                "question": "Qual comando busca comandos shell builtins?",
                "type": "multiple",
                "options": ["type -a", "which", "whereis", "command -V"],
                "correct": 3,
                "explanation": "command -V mostra se comando é builtin, alias ou executável externo."
            },
            {
                "question": "Digite o comando para buscar links simbólicos quebrados:",
                "type": "text",
                "correct": ["find / -type l -xtype l"],
                "explanation": "find / -type l -xtype l encontra links simbólicos quebrados."
            },
        ]
    
    def _get_104_1_questions(self):
        """Criação de Partições e Sistemas de Arquivos (104.1)"""
        return [
            {
                "question": "Qual comando cria sistema de arquivos ext4 em /dev/sdb1?",
                "type": "multiple",
                "options": ["mkfs.ext4", "mke2fs", "format.ext4", "a e b"],
                "correct": 3,
                "explanation": "mkfs.ext4 ou mke2fs -t ext4 criam sistema de arquivos ext4."
            },
            {
                "question": "Digite o comando para criar partição swap:",
                "type": "text",
                "correct": ["mkswap"],
                "explanation": "mkswap /dev/sda2 formata partição como swap."
            },
            {
                "question": "Qual comando cria tabela de partição GPT em disco?",
                "type": "multiple",
                "options": ["parted /dev/sda mklabel gpt", "gdisk /dev/sda", "fdisk -g /dev/sda", "a e b"],
                "correct": 3,
                "explanation": "parted com mklabel gpt ou gdisk criam tabela GPT."
            },
            {
                "question": "Digite o comando para criar partição primária com fdisk:",
                "type": "text",
                "correct": ["n"],
                "explanation": "No fdisk, 'n' cria nova partição, depois 'p' para primária."
            },
            {
                "question": "Qual comando mostra blocos defeituosos em disco?",
                "type": "multiple",
                "options": ["badblocks", "fsck -c", "smartctl", "Todas as anteriores"],
                "correct": 3,
                "explanation": "badblocks verifica blocos ruins. smartctl para SMART. fsck -c verifica durante checagem."
            },
            {
                "question": "Digite o comando para criar sistema de arquivos XFS:",
                "type": "text",
                "correct": ["mkfs.xfs"],
                "explanation": "mkfs.xfs /dev/sdb1 cria sistema de arquivos XFS."
            },
            {
                "question": "Qual comando verifica integridade de sistema de arquivos ext4?",
                "type": "multiple",
                "options": ["fsck.ext4", "e2fsck", "checkfs", "a e b"],
                "correct": 3,
                "explanation": "fsck.ext4 ou e2fsck verificam e reparam ext2/3/4."
            },
            {
                "question": "Digite o comando para criar volume lógico LVM:",
                "type": "text",
                "correct": ["lvcreate"],
                "explanation": "lvcreate -L 10G -n lv_dados vg_sistema cria LV de 10GB."
            },
            {
                "question": "Qual comando cria grupo de volumes LVM?",
                "type": "multiple",
                "options": ["vgcreate", "vgextend", "vgmake", "vginit"],
                "correct": 0,
                "explanation": "vgcreate vg_nome /dev/sda1 /dev/sdb1 cria grupo de volumes."
            },
            {
                "question": "Digite o comando para estender grupo de volumes LVM:",
                "type": "text",
                "correct": ["vgextend"],
                "explanation": "vgextend vg_nome /dev/sdc1 adiciona PV ao VG."
            },
            {
                "question": "Qual comando cria volume físico LVM?",
                "type": "multiple",
                "options": ["pvcreate", "pvmk", "initpv", "lvmcreate"],
                "correct": 0,
                "explanation": "pvcreate /dev/sda1 inicializa partição como volume físico LVM."
            },
            {
                "question": "Digite o comando para redimensionar sistema de arquivos ext4 online:",
                "type": "text",
                "correct": ["resize2fs"],
                "explanation": "resize2fs /dev/vg/lv ajusta tamanho do sistema de arquivos ext4."
            },
            {
                "question": "Qual comando estende volume lógico LVM?",
                "type": "multiple",
                "options": ["lvextend", "lvreduce", "lvresize", "a e c"],
                "correct": 3,
                "explanation": "lvextend -L +5G /dev/vg/lv ou lvresize aumentam LV."
            },
            {
                "question": "Digite o comando para criar sistema de arquivos Btrfs:",
                "type": "text",
                "correct": ["mkfs.btrfs"],
                "explanation": "mkfs.btrfs /dev/sdb1 cria sistema de arquivos Btrfs."
            },
            {
                "question": "Qual utilitário gerencia partições GPT interativamente?",
                "type": "multiple",
                "options": ["gdisk", "cgdisk", "parted", "Todas as anteriores"],
                "correct": 3,
                "explanation": "gdisk (texto), cgdisk (ncurses) e parted gerenciam GPT."
            },
            {
                "question": "Digite o comando para fazer dump de tabela de partições:",
                "type": "text",
                "correct": ["sfdisk -d"],
                "explanation": "sfdisk -d /dev/sda > backup.txt faz backup da tabela de partições."
            },
            {
                "question": "Qual comando restaura tabela de partições de backup?",
                "type": "multiple",
                "options": ["sfdisk /dev/sda < backup.txt", "fdisk -r backup.txt", "parted restore", "dd if=backup.txt of=/dev/sda"],
                "correct": 0,
                "explanation": "sfdisk /dev/sda < backup.txt restaura tabela de partições."
            },
            {
                "question": "Digite o comando para criar sistema de arquivos FAT32:",
                "type": "text",
                "correct": ["mkfs.vfat", "mkfs.fat"],
                "explanation": "mkfs.vfat -F 32 /dev/sdb1 cria FAT32."
            },
            {
                "question": "Qual comando define UUID para sistema de arquivos?",
                "type": "multiple",
                "options": ["tune2fs -U", "xfs_admin -U", "btrfstune -U", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Cada sistema de arquivos tem seu comando para alterar UUID."
            },
            {
                "question": "Digite o comando para criar partição swap e ativá-la:",
                "type": "text",
                "correct": ["mkswap && swapon"],
                "explanation": "mkswap /dev/sda2 && swapon /dev/sda2 cria e ativa swap."
            },
            {
                "question": "Qual utilitário particiona discos grandes (>2TB) em RedHat?",
                "type": "multiple",
                "options": ["parted", "gdisk", "anaconda", "Todas as anteriores"],
                "correct": 3,
                "explanation": "parted e gdisk para linha de comando, anaconda para instalação."
            },
            {
                "question": "Digite o comando para ver UUID de partições:",
                "type": "text",
                "correct": ["blkid", "lsblk -f"],
                "explanation": "blkid ou lsblk -f mostram UUIDs das partições."
            },
            {
                "question": "Qual comando marca partição como ativa (bootável)?",
                "type": "multiple",
                "options": ["fdisk: a", "parted: set 1 boot on", "sfdisk -A", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Em fdisk: 'a'. Em parted: 'set 1 boot on'. sfdisk -A 1."
            },
            {
                "question": "Digite o comando para verificar partição swap:",
                "type": "text",
                "correct": ["swapon -s", "free", "cat /proc/swaps"],
                "explanation": "swapon -s, free ou /proc/swaps mostram swap ativa."
            },
            {
                "question": "Qual comando cria sistema de arquivos NTFS no Linux?",
                "type": "multiple",
                "options": ["mkfs.ntfs", "ntfs-3g (com -f)", "mkntfs", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Várias ferramentas criam NTFS: mkfs.ntfs, ntfs-3g -f, mkntfs."
            },
        ]
    
    def _get_104_2_questions(self):
        """Manutenção da Integridade de Sistemas de Arquivos (104.2)"""
        return [
            {
                "question": "Qual comando verifica sistema de arquivos ext4?",
                "type": "multiple",
                "options": ["fsck.ext4", "e2fsck", "checkfs", "a e b"],
                "correct": 3,
                "explanation": "fsck.ext4 ou e2fsck verificam e reparam sistemas ext2/3/4."
            },
            {
                "question": "Digite o comando para forçar verificação no próximo boot:",
                "type": "text",
                "correct": ["touch /forcefsck"],
                "explanation": "touch /forcefsck (sistemas SysV) força fsck no próximo boot."
            },
            {
                "question": "Como marcar sistema de arquivos para verificação periódica?",
                "type": "multiple",
                "options": ["tune2fs -i", "tune2fs -c", "chkfs", "fsck --interval"],
                "correct": 0,
                "explanation": "tune2fs -i 30d /dev/sda1 força verificação a cada 30 dias."
            },
            {
                "question": "Digite o comando para verificar XFS:",
                "type": "text",
                "correct": ["xfs_repair"],
                "explanation": "xfs_repair verifica e repara sistema de arquivos XFS."
            },
            {
                "question": "Qual comando mostra informações de superbloco ext4?",
                "type": "multiple",
                "options": ["dumpe2fs", "tune2fs -l", "debugfs", "a e b"],
                "correct": 3,
                "explanation": "dumpe2fs /dev/sda1 ou tune2fs -l /dev/sda1 mostram informações."
            },
            {
                "question": "Digite o comando para ver contagem de mounts entre verificações:",
                "type": "text",
                "correct": ["tune2fs -l | grep Mount", "dumpe2fs | grep Mount"],
                "explanation": "tune2fs -l mostra 'Mount count' e 'Maximum mount count'."
            },
            {
                "question": "Como desabilitar verificação após N mounts?",
                "type": "multiple",
                "options": ["tune2fs -c 0", "tune2fs -i 0", "fsck -D", "chattr +nocheck"],
                "correct": 0,
                "explanation": "tune2fs -c 0 /dev/sda1 desabilita verificação baseada em contagem de mounts."
            },
            {
                "question": "Digite o comando para restaurar superbloco backup ext4:",
                "type": "text",
                "correct": ["e2fsck -b", "fsck.ext4 -B"],
                "explanation": "e2fsck -b 32768 /dev/sda1 usa superbloco backup (32768 é comum)."
            },
            {
                "question": "Qual comando mostra blocos defeituosos em disco?",
                "type": "multiple",
                "options": ["badblocks", "smartctl -t long", "fsck -c", "Todas as anteriores"],
                "correct": 3,
                "explanation": "badblocks verifica. smartctl testa SMART. fsck -c verifica durante fsck."
            },
            {
                "question": "Digite o comando para marcar blocos ruins automaticamente:",
                "type": "text",
                "correct": ["e2fsck -c", "fsck.ext4 -c"],
                "explanation": "e2fsck -c /dev/sda1 verifica e marca blocos ruins."
            },
            {
                "question": "Qual arquivo contém sistemas de arquivos a verificar no boot?",
                "type": "multiple",
                "options": ["/etc/fstab", "/etc/mtab", "/proc/filesystems", "/etc/filesystems"],
                "correct": 0,
                "explanation": "Coluna 6 no /etc/fstab define ordem de verificação (0=skip, 1=root, 2=outros)."
            },
            {
                "question": "Digite a opção do fsck para reparar automaticamente:",
                "type": "text",
                "correct": ["-a", "-p"],
                "explanation": "fsck -a ou -p reparam automaticamente sem perguntar."
            },
            {
                "question": "Qual comando verifica Btrfs?",
                "type": "multiple",
                "options": ["btrfs check", "fsck.btrfs", "btrfsck", "checkbtrfs"],
                "correct": 0,
                "explanation": "btrfs check /dev/sda1 verifica integridade Btrfs."
            },
            {
                "question": "Digite o comando para verificar sistema de arquivos montado readonly:",
                "type": "text",
                "correct": ["fsck -n", "e2fsck -n"],
                "explanation": "fsck -n verifica modo readonly, sem fazer alterações."
            },
            {
                "question": "Qual comando mostra journal do sistema de arquivos?",
                "type": "multiple",
                "options": ["dumpe2fs -j", "debugfs", "journalctl", "jls"],
                "correct": 0,
                "explanation": "dumpe2fs -j /dev/sda1 mostra informações do journal ext4."
            },
            {
                "question": "Digite o comando para desfragmentar sistema de arquivos ext4:",
                "type": "text",
                "correct": ["e4defrag"],
                "explanation": "e4defrag /caminho desfragmenta arquivos/diretórios específicos."
            },
            {
                "question": "Como verificar integridade de arquivo específico em Btrfs?",
                "type": "multiple",
                "options": ["btrfs scrub", "btrfs check --file", "btrfs verify", "btrfs integrity"],
                "correct": 0,
                "explanation": "btrfs scrub inicia verificação de integridade em Btrfs montado."
            },
            {
                "question": "Digite o comando para corrigir erros automaticamente no fsck:",
                "type": "text",
                "correct": ["fsck -y"],
                "explanation": "fsck -y responde 'yes' a todas as perguntas durante reparo."
            },
            {
                "question": "Qual arquivo lista sistemas de arquivos atualmente montados?",
                "type": "multiple",
                "options": ["/proc/mounts", "/etc/mtab", "/proc/self/mounts", "Todas as anteriores"],
                "correct": 3,
                "explanation": "/proc/mounts (kernel), /etc/mtab (usuário), /proc/self/mounts."
            },
            {
                "question": "Digite o comando para ver status de verificação de disco agendada:",
                "type": "text",
                "correct": ["systemd-analyze", "uptime", "last fsck", "journalctl | grep fsck"],
                "explanation": "journalctl | grep -i fsck ou systemd-analyze blame mostra tempo de fsck no boot."
            },
            {
                "question": "Qual utilitário verifica discos via SMART?",
                "type": "multiple",
                "options": ["smartctl", "badblocks", "hdparm -t", "disktest"],
                "correct": 0,
                "explanation": "smartctl -a /dev/sda mostra atributos SMART do disco."
            },
            {
                "question": "Digite o comando para testar leitura de disco:",
                "type": "text",
                "correct": ["hdparm -tT", "dd if=/dev/sda of=/dev/null bs=1M count=100"],
                "explanation": "hdparm -tT testa cache e leitura. dd testa velocidade de transferência."
            },
            {
                "question": "Como verificar sistema de arquivos raiz?",
                "type": "multiple",
                "options": ["Usar Live CD/DVD", "boot em single user", "fsck na inicialização", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Sistema raiz deve estar desmontado para fsck completo."
            },
            {
                "question": "Digite o comando para visualizar uso de inodes:",
                "type": "text",
                "correct": ["df -i"],
                "explanation": "df -i mostra uso de inodes em vez de espaço em disco."
            },
            {
                "question": "Qual comando limpa journal do sistema de arquivos?",
                "type": "multiple",
                "options": ["tune2fs -O ^has_journal", "debugfs -w -R 'feature -has_journal'", "Ambas", "Nenhuma"],
                "correct": 2,
                "explanation": "Ambos comandos desabilitam journal. Use com extremo cuidado!"
            },
        ]
    
    def _get_104_3_questions(self):
        """Montagem e Desmontagem de Sistemas de Arquivos (104.3)"""
        return [
            {
                "question": "Qual comando monta sistema de arquivos?",
                "type": "multiple",
                "options": ["mount", "umount", "fsmount", "mnt"],
                "correct": 0,
                "explanation": "mount /dev/sdb1 /mnt monta partição no diretório /mnt."
            },
            {
                "question": "Digite o comando para desmontar sistema de arquivos:",
                "type": "text",
                "correct": ["umount", "unmount"],
                "explanation": "umount /mnt ou umount /dev/sdb1 desmontam."
            },
            {
                "question": "Qual arquivo define montagens automáticas?",
                "type": "multiple",
                "options": ["/etc/fstab", "/etc/mtab", "/proc/mounts", "/etc/filesystems"],
                "correct": 0,
                "explanation": "/etc/fstab define sistemas de arquivos montados automaticamente no boot."
            },
            {
                "question": "Digite o comando para remontar sistema de arquivos como readonly:",
                "type": "text",
                "correct": ["mount -o remount,ro"],
                "explanation": "mount -o remount,ro /mnt remonta como somente leitura."
            },
            {
                "question": "Qual comando lista sistemas de arquivos montados?",
                "type": "multiple",
                "options": ["mount", "df", "findmnt", "Todas as anteriores"],
                "correct": 3,
                "explanation": "mount sem argumentos, df -h, findmnt listam montagens."
            },
            {
                "question": "Digite o comando para montar partição usando UUID:",
                "type": "text",
                "correct": ["mount UUID=xxx /mnt"],
                "explanation": "mount UUID='1234-ABCD' /mnt monta usando UUID."
            },
            {
                "question": "Qual opção do mount força montagem mesmo com erros?",
                "type": "multiple",
                "options": ["-f", "--force", "Não existe, usa -o force", "-o force"],
                "correct": 0,
                "explanation": "mount -f força montagem (faz nada realmente, apenas debug)."
            },
            {
                "question": "Digite o comando para montar todos os sistemas de /etc/fstab:",
                "type": "text",
                "correct": ["mount -a"],
                "explanation": "mount -a monta todos os sistemas de arquivos do fstab."
            },
            {
                "question": "Qual comando desmonta sistema de arquivos ocupado?",
                "type": "multiple",
                "options": ["umount -l", "umount -f", "fuser -k", "Todas as anteriores"],
                "correct": 3,
                "explanation": "umount -l lazy unmount. umount -f força. fuser -k mata processos."
            },
            {
                "question": "Digite o comando para ver quais processos estão usando mount point:",
                "type": "text",
                "correct": ["lsof /mnt", "fuser -m /mnt"],
                "explanation": "lsof /mnt ou fuser -m /mnt mostram processos usando o diretório."
            },
            {
                "question": "Qual opção do mount permite execução de binários?",
                "type": "multiple",
                "options": ["-o exec", "-o noexec", "padrão permite execução", "-x"],
                "correct": 2,
                "explanation": "Por padrão, mount permite execução. -o noexec desabilita."
            },
            {
                "question": "Digite a linha /etc/fstab para montar NFS:",
                "type": "text",
                "correct": ["servidor:/export /mnt nfs defaults 0 0"],
                "explanation": "servidor:/caminho /local nfs opts dump pass"
            },
            {
                "question": "Qual opção do mount monta como somente leitura?",
                "type": "multiple",
                "options": ["-o ro", "-r", "-o readonly", "Todas as anteriores"],
                "correct": 3,
                "explanation": "-r, -o ro, -o readonly montam como somente leitura."
            },
            {
                "question": "Digite o comando para montar imagem ISO:",
                "type": "text",
                "correct": ["mount -o loop arquivo.iso /mnt"],
                "explanation": "mount -o loop arquivo.iso /mnt monta imagem ISO."
            },
            {
                "question": "Qual comando mostra opções de montagem atuais?",
                "type": "multiple",
                "options": ["mount | grep /mnt", "findmnt -o OPTIONS /mnt", "cat /proc/mounts", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Várias formas de ver opções de montagem atuais."
            },
            {
                "question": "Digite o comando para montar CIFS/SMB:",
                "type": "text",
                "correct": ["mount -t cifs"],
                "explanation": "mount -t cifs //servidor/share /mnt -o user=nome monta share Windows/Samba."
            },
            {
                "question": "Qual arquivo contém sistemas de arquivos suportados?",
                "type": "multiple",
                "options": ["/proc/filesystems", "/etc/filesystems", "/lib/modules/*/kernel/fs/", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Vários lugares definem sistemas de arquivos suportados pelo kernel."
            },
            {
                "question": "Digite a opção do mount para usuário comum poder montar:",
                "type": "text",
                "correct": ["-o user"],
                "explanation": "mount -o user permite que usuários não-root montem."
            },
            {
                "question": "Qual comando configura quota em sistema de arquivos montado?",
                "type": "multiple",
                "options": ["quotaon", "mount -o quota", "edquota", "Todas as anteriores"],
                "correct": 3,
                "explanation": "montar com -o quota, depois quotaon, edquota configura."
            },
            {
                "question": "Digite o comando para montar tmpfs:",
                "type": "text",
                "correct": ["mount -t tmpfs tmpfs /mnt/tmp"],
                "explanation": "mount -t tmpfs -o size=1G tmpfs /mnt/tmp monta filesystem em RAM."
            },
            {
                "question": "Qual opção do mount sincroniza escritas imediatamente?",
                "type": "multiple",
                "options": ["-o sync", "-o async", "-o writeback", "-o barrier"],
                "correct": 0,
                "explanation": "-o sync força sincronização (mais lento, mais seguro)."
            },
            {
                "question": "Digite a ordem de campos no /etc/fstab:",
                "type": "text",
                "correct": ["dispositivo ponto_montagem tipo opções dump pass"],
                "explanation": "device mountpoint fstype options dump pass"
            },
            {
                "question": "Qual comando mostra espaço livre em montagens?",
                "type": "multiple",
                "options": ["df", "mount -s", "free", "du"],
                "correct": 0,
                "explanation": "df -h mostra espaço livre em sistemas de arquivos montados."
            },
            {
                "question": "Digite o comando para remontar com novas opções:",
                "type": "text",
                "correct": ["mount -o remount,opções"],
                "explanation": "mount -o remount,rw /mnt muda para leitura/escrita sem desmontar."
            },
            {
                "question": "Qual sistema monta automaticamente dispositivos em /media/?",
                "type": "multiple",
                "options": ["udisks/udisks2", "autofs", "systemd-mount", "Todas as anteriores"],
                "correct": 3,
                "explanation": "Vários sistemas para montagem automática: udisks, autofs, systemd."
            },
        ]
    
    def get_random_questions(self, topic: str, num: int = 5) -> List[Dict]:
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
        self.root.geometry("900x700")
        
          # Tenta carregar ícone Linux
        try:
            # Para Windows: .ico
            self.root.iconbitmap('linux_icon.ico')
        except:
            try:
                # Para Linux: .xbm ou .png
                self.root.iconphoto(True, tk.PhotoImage(file='linux_icon.png'))
            except:
                # Se não encontrar arquivo, usa ícone embutido
                try:
                    from base64 import b64decode
                    import tempfile
                    import os
                    
                    # Decodifica ícone base64 e salva temporariamente
                    icon_data = b64decode(linux_icon_base64.replace('\n', ''))
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.ico')
                    temp_file.write(icon_data)
                    temp_file.close()
                    
                    self.root.iconbitmap(temp_file.name)
                    # Não deleta imediatamente para o ícone permanecer durante execução
                    os.unlink(temp_file.name)
                except:
                    # Se tudo falhar, usa ícone padrão do Tkinter
                    pass
        
        # Banco de questões
        self.question_bank = QuestionBank()
        
        # Variáveis de controle
        self.current_topic = tk.StringVar()
        self.current_question_index = 0
        self.current_questions = []
        self.score = 0
        self.total_questions = 0
        self.user_answers = {}
        
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
        
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="LPIC-1 Sistema de Estudo", 
            font=("Arial", 20, "bold"),
            foreground=self.primary_color
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Subtítulo
        subtitle_label = ttk.Label(
            main_frame,
            text="Tópicos 101 a 104 - Preparação para Certificação Linux",
            font=("Arial", 11)
        )
        subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # Controles de tópico
        ttk.Label(main_frame, text="Selecione o Tópico:").grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.topic_combo = ttk.Combobox(
            main_frame, 
            textvariable=self.current_topic,
            state="readonly",
            width=50
        )
        self.topic_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(5, 10), pady=5)
        
        self.start_btn = ttk.Button(
            main_frame, 
            text="Iniciar Teste", 
            command=self.start_test,
            width=15
        )
        self.start_btn.grid(row=2, column=2, padx=5, pady=5)
        
        # Frame da questão
        self.question_frame = ttk.LabelFrame(main_frame, text="Questão", padding="15")
        self.question_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 10))
        self.question_frame.columnconfigure(0, weight=1)
        
        self.question_label = tk.Text(
            self.question_frame, 
            height=4,
            wrap=tk.WORD,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg=self.bg_color
        )
        self.question_label.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Frame de resposta (será configurado dinamicamente)
        self.answer_frame = ttk.Frame(self.question_frame)
        self.answer_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        self.answer_frame.columnconfigure(0, weight=1)
        
        # Frame de botões de navegação
        nav_frame = ttk.Frame(self.question_frame)
        nav_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.prev_btn = ttk.Button(
            nav_frame, 
            text="← Anterior", 
            command=self.prev_question,
            state="disabled"
        )
        self.prev_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.next_btn = ttk.Button(
            nav_frame, 
            text="Próxima →", 
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        self.submit_btn = ttk.Button(
            nav_frame, 
            text="Enviar Resposta", 
            command=self.submit_answer,
            state="disabled"
        )
        self.submit_btn.pack(side=tk.LEFT, padx=5)
        
        self.finish_btn = ttk.Button(
            nav_frame,
            text="Finalizar Teste",
            command=self.finish_test,
            state="disabled"
        )
        self.finish_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame de explicação
        self.explanation_frame = ttk.LabelFrame(main_frame, text="Explicação", padding="10")
        self.explanation_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        self.explanation_frame.columnconfigure(0, weight=1)
        self.explanation_frame.rowconfigure(0, weight=1)
        
        self.explanation_text = scrolledtext.ScrolledText(
            self.explanation_frame,
            height=8,
            wrap=tk.WORD,
            font=("Arial", 10),
            relief=tk.FLAT,
            bg=self.bg_color,
            state=tk.DISABLED
        )
        self.explanation_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Selecione um tópico e clique em 'Iniciar Teste'")
        
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=(5, 2)
        )
        status_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(20, 0))
        
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
        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete(1.0, tk.END)
        self.explanation_text.config(state=tk.DISABLED)
        
        if self.current_question_index >= len(self.current_questions):
            return
        
        question = self.current_questions[self.current_question_index]
        
        # Mostrar texto da questão
        self.question_label.config(state=tk.NORMAL)
        self.question_label.delete(1.0, tk.END)
        self.question_label.insert(1.0, question["question"])
        self.question_label.config(state=tk.DISABLED)
        
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
        self.user_answer_var = tk.StringVar()
        
        for i, option in enumerate(question["options"]):
            rb = ttk.Radiobutton(
                self.answer_frame,
                text=option,
                variable=self.user_answer_var,
                value=str(i),
                style="TRadiobutton"
            )
            rb.grid(row=i, column=0, sticky=tk.W, pady=2)
        
        # Se já respondeu, marcar a resposta
        if self.current_question_index in self.user_answers:
            self.user_answer_var.set(self.user_answers[self.current_question_index])
    
    def setup_text_answer(self, question):
        """Configura interface para questão de resposta textual"""
        ttk.Label(self.answer_frame, text="Sua resposta:").grid(row=0, column=0, sticky=tk.W, pady=2)
        
        self.text_answer_var = tk.StringVar()
        text_entry = ttk.Entry(
            self.answer_frame,
            textvariable=self.text_answer_var,
            width=50
        )
        text_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
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
        
        # Atualizar pontuação
        if is_correct and self.current_question_index not in getattr(self, 'scored_questions', []):
            self.score += 1
            if not hasattr(self, 'scored_questions'):
                self.scored_questions = []
            self.scored_questions.append(self.current_question_index)
        
        # Mostrar feedback
        self.show_answer_feedback()
        
        # Atualizar status
        self.status_var.set(
            f"Resposta submetida. "
            f"Pontuação: {self.score}/{self.total_questions}. "
            f"Questão {self.current_question_index + 1} de {self.total_questions}"
        )
    
    def show_answer_feedback(self):
        """Mostra feedback da resposta"""
        if self.current_question_index not in self.user_answers:
            return
        
        question = self.current_questions[self.current_question_index]
        user_answer = self.user_answers[self.current_question_index]
        
        # Determinar se está correta
        is_correct = False
        correct_answer = ""
        
        if question["type"] == "multiple":
            is_correct = (int(user_answer) == question["correct"])
            correct_answer = question["options"][question["correct"]]
        elif question["type"] == "text":
            correct_answers = [ans.lower() for ans in question["correct"]]
            is_correct = (user_answer.lower() in correct_answers)
            correct_answer = " ou ".join(question["correct"])
        
        # Mostrar explicação
        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete(1.0, tk.END)
        
        # Adicionar cabeçalho colorido
        if is_correct:
            self.explanation_text.insert(1.0, "✓ CORRETO\n\n", "correct")
        else:
            self.explanation_text.insert(1.0, "✗ INCORRETO\n\n", "wrong")
        
        # Mostrar resposta correta
        if question["type"] == "multiple":
            self.explanation_text.insert(tk.END, f"Resposta correta: {correct_answer}\n\n")
        elif question["type"] == "text":
            self.explanation_text.insert(tk.END, f"Resposta(s) correta(s): {correct_answer}\n\n")
        
        # Mostrar explicação
        self.explanation_text.insert(tk.END, f"Explicação: {question['explanation']}")
        
        # Configurar tags para cores
        self.explanation_text.tag_config("correct", foreground=self.correct_color, font=("Arial", 10, "bold"))
        self.explanation_text.tag_config("wrong", foreground=self.wrong_color, font=("Arial", 10, "bold"))
        
        self.explanation_text.config(state=tk.DISABLED)
        
        # Destacar widgets de resposta
        if question["type"] == "multiple":
            for widget in self.answer_frame.winfo_children():
                if isinstance(widget, ttk.Radiobutton):
                    if widget['value'] == user_answer:
                        if is_correct:
                            widget.configure(style="Correct.TRadiobutton")
                        else:
                            widget.configure(style="Wrong.TRadiobutton")
                    elif widget['value'] == str(question["correct"]):
                        widget.configure(style="Correct.TRadiobutton")
    
    def prev_question(self):
        """Vai para a questão anterior"""
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()
            self.status_var.set(f"Questão {self.current_question_index + 1} de {self.total_questions}")
    
    def next_question(self):
        """Vai para a próxima questão"""
        if self.current_question_index < len(self.current_questions) - 1:
            self.current_question_index += 1
            self.show_question()
            self.status_var.set(f"Questão {self.current_question_index + 1} de {self.total_questions}")
    
    def update_navigation(self):
        """Atualiza estado dos botões de navegação"""
        self.prev_btn['state'] = 'normal' if self.current_question_index > 0 else 'disabled'
        self.next_btn['state'] = 'normal' if self.current_question_index < len(self.current_questions) - 1 else 'disabled'
        
        # Desabilitar submit se já respondeu
        if self.current_question_index in self.user_answers:
            self.submit_btn['state'] = 'disabled'
        else:
            self.submit_btn['state'] = 'normal'
    
    def finish_test(self):
        """Finaliza o teste e mostra resultados"""
        # Contar questões respondidas
        answered = len(self.user_answers)
        total = self.total_questions
        
        # Calcular porcentagem
        percentage = (self.score / total * 100) if total > 0 else 0
        
        # Mostrar resultados
        result_msg = (
            f"Teste Finalizado!\n\n"
            f"Tópico: {self.current_topic.get()}\n"
            f"Questões respondidas: {answered}/{total}\n"
            f"Pontuação: {self.score}/{total}\n"
            f"Porcentagem: {percentage:.1f}%\n\n"
        )
        
        # Adicionar mensagem baseada no desempenho
        if percentage >= 80:
            result_msg += "Excelente! Você está preparado para este tópico."
        elif percentage >= 60:
            result_msg += "Bom trabalho! Continue estudando."
        else:
            result_msg += "Recomenda-se revisar o material e tentar novamente."
        
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
        
        # Limpar interface
        self.question_label.config(state=tk.NORMAL)
        self.question_label.delete(1.0, tk.END)
        self.question_label.config(state=tk.DISABLED)
        
        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete(1.0, tk.END)
        self.explanation_text.config(state=tk.DISABLED)
        
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
    
    # Configurar estilo adicional
    style = ttk.Style()
    style.configure("Correct.TRadiobutton", foreground="#27ae60")
    style.configure("Wrong.TRadiobutton", foreground="#e74c3c")
    
    # Iniciar aplicação
    root.mainloop()


if __name__ == "__main__":
    main()