/*!
 * @file rt_serial.h
 * @brief Serial port
 */

#ifndef _rt_serial
#define _rt_serial

__BEGIN_DECLS

/* Perform the I/O control operation specified by REQUEST on FD.
   One argument may follow; its presence and type depend on REQUEST.
   Return value depends on REQUEST.  Usually -1 indicates error.  */
extern int ioctl (int __fd, unsigned long int __request, ...) __THROW;

__END_DECLS

int set_interface_attribs_custom_baud(int fd, int speed, int parity, int port);
void init_serial_for_sbus(int fd, int baud);

#endif
