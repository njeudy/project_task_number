# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

class projectTask(osv.osv):
    _name = "project.task"
    _inherit = "project.task"

    _columns = {
        'ref':fields.char('Reference', size=64, translate=False, ),
    }

    _defaults = {
        'ref': _('NEW'),
    }

    def create(self, cr, uid, vals, context=None):
        vals.update({
            'ref': self.pool.get('ir.sequence').get(cr, uid, 'project.task_ref')
        })
        return super(projectTask, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        ctx = context.copy()
        if self.browse(cr, uid, ids, context=ctx)[0]['ref'] == 'NEW':
            vals.update({
                'ref': self.pool.get('ir.sequence').get(cr, uid, 'project.task_ref')
            })
        return super(projectTask, self).write(cr, uid, ids, vals, context=ctx)
