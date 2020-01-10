/* -*- Mode: C; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- */
/*
 * mbimcli -- Command line interface to control MBIM devices
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Copyright (C) 2013 Aleksander Morgado <aleksander@gnu.org>
 */

#include <glib.h>

#ifndef __MBIMCLI_H__
#define __MBIMCLI_H__

/* Common */
void mbimcli_async_operation_done (gboolean operation_status);

/* Basic Connect group */
GOptionGroup *mbimcli_basic_connect_get_option_group (void);
gboolean      mbimcli_basic_connect_options_enabled  (void);
void          mbimcli_basic_connect_run              (MbimDevice *device,
                                                      GCancellable *cancellable);


#endif /* __MBIMCLI_H__ */
