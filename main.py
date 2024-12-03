from controllers.main_controller import MainController
from views.view_manager import ViewManager


def main():
    view_manager = ViewManager()
    main_controller = MainController(view_manager)
    main_controller.run()

if __name__ == "__main__":
    main()

# import threading
# import time
# from rich.console import Console
# from rich.table import Table
# from rich.live import Live
#
# console = Console()
#
# def create_table(texte1, texte2, clignoter=True):
#     """
#     Crée une table avec les textes spécifiés.
#
#     :param texte1: Texte clignotant.
#     :param texte2: Texte fixe.
#     :param clignoter: Booléen pour déterminer si le texte clignote ou non.
#     :return: Table Rich avec le texte combiné.
#     """
#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("Texte Combiné")
#
#     # Texte combiné avec option de clignotement
#     if clignoter:
#         texte_combine = f"[bold blue]{texte1}[/bold blue] [bold yellow]{texte2}[/bold yellow]"
#     else:
#         texte_combine = f"{' ' * len(texte1)} [bold yellow]{texte2}[/bold yellow]"
#
#     table.add_row(texte_combine)
#     return table
#
# def clignoter_texte(live, texte1, texte2, frequence=0.5, stop_event=None):
#     """
#     Fonction pour faire clignoter un texte dans le terminal.
#
#     :param live: Live Rich pour la mise à jour en continu.
#     :param texte1: Texte clignotant.
#     :param texte2: Texte fixe.
#     :param frequence: Intervalle de clignotement (en secondes).
#     :param stop_event: threading.Event utilisé pour arrêter l'animation.
#     """
#     while not stop_event.is_set():
#         # Texte clignotant visible
#         table = create_table(texte1, texte2, clignoter=True)
#         live.update(table)
#         time.sleep(frequence)
#
#         # Texte clignotant caché
#         table = create_table(texte1, texte2, clignoter=False)
#         live.update(table)
#         time.sleep(frequence)
#
# if __name__ == "__main__":
#     texte1 = "Bonjour"
#     texte2 = "Monde"
#     stop_event = threading.Event()
#
#     # Utiliser Live pour la mise à jour dynamique du tableau
#     with Live(auto_refresh=True, refresh_per_second=10) as live:
#         # Démarrer l'animation dans un thread séparé
#         thread_animation = threading.Thread(target=clignoter_texte, args=(live, texte1, texte2, 0.5, stop_event))
#         thread_animation.start()
#
#         try:
#             # Saisie utilisateur pour arrêter l'animation
#             input("Appuyez sur Entrée pour arrêter le clignotement...\n")
#         finally:
#             # Signale l'arrêt de l'animation
#             stop_event.set()
#
#         # Attendre que le thread d'animation se termine
#         thread_animation.join()
#
#         console.print("Clignotement arrêté.")