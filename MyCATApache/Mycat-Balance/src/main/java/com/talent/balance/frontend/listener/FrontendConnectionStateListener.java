/*
 * Copyright (c) 2013, OpenCloudDB/MyCAT and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software;Designed and Developed mainly by many Chinese 
 * opensource volunteers. you can redistribute it and/or modify it under the 
 * terms of the GNU General Public License version 2 only, as published by the
 * Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 * 
 * Any questions about this component can be directed to it's project Web address 
 * https://code.google.com/p/opencloudb/.
 *
 */
package com.talent.balance.frontend.listener;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.talent.balance.backend.BackendStarter;
import com.talent.balance.mapping.Mapping;
import com.talent.nio.communicate.ChannelContext;
import com.talent.nio.listener.ConnectionStateListener;

/**
 * 
 * @filename:	 com.talent.balance.frontend.listener.FrontendConnectionStateListener
 * @copyright:   Copyright (c)2010
 * @company:     talent
 * @author:      谭耀武
 * @version:     1.0
 * @create time: 2013年12月23日 上午9:28:21
 * @record
 * <table cellPadding="3" cellSpacing="0" style="width:600px">
 * <thead style="font-weight:bold;background-color:#e3e197">
 * 	<tr>   <td>date</td>	<td>author</td>		<td>version</td>	<td>description</td></tr>
 * </thead>
 * <tbody style="background-color:#ffffeb">
 * 	<tr><td>2013年12月23日</td>	<td>谭耀武</td>	<td>1.0</td>	<td>create</td></tr>
 * </tbody>
 * </table>
 */
public class FrontendConnectionStateListener implements ConnectionStateListener
{
	@SuppressWarnings("unused")
	private static Logger log = LoggerFactory.getLogger(FrontendConnectionStateListener.class);

	/**
	 * 
	 */
	public FrontendConnectionStateListener()
	{

	}

	/**
	 * @param args
	 */
	public static void main(String[] args)
	{

	}

	@Override
	public void onTcpOff(ChannelContext channelContext)
	{

	}

	@Override
	public void onTcpBuilding(ChannelContext channelContext)
	{

	}

	@Override
	public void onTcpOn(ChannelContext channelContext) throws Exception
	{
		BackendStarter.registerFrontendClient(channelContext);
	}

	@Override
	public void onTcpLinkFailed(ChannelContext channelContext)
	{

	}

	@Override
	public void onAppOff(ChannelContext channelContext)
	{

	}

	@Override
	public void onAppBuilding(ChannelContext channelContext)
	{

	}

	@Override
	public void onAppOn(ChannelContext channelContext)
	{

	}

	@Override
	public void onAppLinkFailed(ChannelContext channelContext)
	{

	}

	@Override
	public void onLogouting(ChannelContext channelContext)
	{

	}

	@Override
	public void onRemoved(ChannelContext channelContext) throws Exception
	{
		Mapping.remove(channelContext);

	}

}