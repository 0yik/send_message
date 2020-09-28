from odoo.models import AbstractModel


class Base(AbstractModel):
    """The base model, which is implicitly inherited by all models.
    """
    _inherit = "base"

    def send_message_user(self, user_id, message):
        """
        Get mail.channel user then run message_post
        :param user_id: id user to send message
        :param message: text to be sent
        """
        channel_obj = self.env['mail.channel']
        partner_id = self.env['res.users'].browse(user_id).partner_id.id
        channel_id = channel_obj.channel_get([partner_id]).get('id')

        kwargs = {
            "partner_ids": [],
            "channel_ids": [],
            "body": message,
            "attachment_ids": [],
            "canned_response_ids": [],
            "message_type": "comment",
            "subtype": "mail.mt_comment",
        }
        channel_obj.browse(channel_id).message_post(**kwargs)