import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction

logger = logging.getLogger(__name__)

CMD_LOCKSCREEN = '''cinnamon-screensaver-command -l'''

class ScreenLockerExtension(Extension):

    def __init__(self):
        super(ScreenLockerExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Lock screen',
                                         on_enter=RunScriptAction(CMD_LOCKSCREEN, [])))

        return RenderResultListAction(items)

if __name__ == '__main__':
    ScreenLockerExtension().run()
