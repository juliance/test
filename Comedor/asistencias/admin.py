# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from customform import *
from models import *
from forms import *

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_per_page = 600
    list_display = ['nombre', 'apellido_1', 'apellido_2', 'centro','comedor_default','come_default']
    list_display_links = ['nombre', 'apellido_1', 'apellido_2']
    list_filter = ['tipo','comedor_default', 'centro']
    search_fields = ['nombre', 'apellido_1', 'apellido_2']
    list_editable = ['centro','comedor_default','come_default']

class AsistenciasAdmin(CustomInlineAdmin):
    model = asistencia
    extra = 0


@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'centro', 'turno', 'observaciones']
    list_filter = ['fecha', 'centro', 'turno']
    inlines = [ AsistenciasAdmin ]
    form = DiarioForm
    #exclude = ['centro']

    def get_queryset(self, request):
        qs = super(DiarioAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(centro = Responsable.objects.get(user=request.user.pk).centro)
        else:
            return qs

    def add_view(self, request, form_url='', extra_context=None):
        data = request.GET.copy()
        data['centro'] = Responsable.objects.get(user=request.user.pk).centro.pk
        request.GET = data
        return super(DiarioAdmin, self).add_view(request, form_url="", extra_context=extra_context)

    def _create_formsets(self, request, obj, change):
        """datos iniciales que no están en la base de datos"""
        formsets = []
        inline_instances = []
        prefixes = {}
        get_formsets_args = [request]

        if change:
            get_formsets_args.append(obj)
        for FormSet, inline in self.get_formsets_with_inlines(*get_formsets_args):
            prefix = FormSet.get_default_prefix()
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
            if prefixes[prefix] != 1 or not prefix:
                prefix = "%s-%s" % (prefix, prefixes[prefix])
            formset_params = {
                'instance': obj,
                'prefix': prefix,
                'queryset': inline.get_queryset(request),
            }
            if request.method == 'POST':
                formset_params.update({
                    'data': request.POST,
                    'files': request.FILES,
                    'save_as_new': '_saveasnew' in request.POST
                })
            if change:
                formsets.append(FormSet(**formset_params))
                inline_instances.append(inline)
            else:
                if isinstance(inline, AsistenciasAdmin):
                    current_user_centro = Responsable.objects.get(user=request.user.pk).centro.pk
                    lUser = Usuario.objects.filter(centro__id = current_user_centro)
                    inline_initial_data = []
                    for dUser in lUser:
                        inline_initial_data += [{
                            'usuario'       : dUser,
                            'comedor'       : dUser.comedor_default,
                            'dieta'         : dUser.dieta_default,
                            'presentacion'  : dUser.presentacion_default,
                            'come'          : dUser.come_default,
                        }]


                    formset_params['initial'] = inline_initial_data
                    formsets.append(FormSet(**formset_params))
                    inline_instances.append(inline)
                else:
                    formsets.append(FormSet(**formset_params))
                    inline_instances.append(inline)

        return formsets, inline_instances

admin.site.register({Centro, Comedor, incidencia})

class ResponsableAdmin(admin.StackedInline):
    model = Responsable
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ResponsableAdmin, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
