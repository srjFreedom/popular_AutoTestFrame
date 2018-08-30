# -*- coding:utf8 -*-

from lib.proto.proto_base import *


class S2C_ACCNAME():

    def s2c_login(self, s2c):
        """
        登录协议
        :param data: 登录协议二进制数据
        :return: 返回解析后的协议信息数据
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.time)
        return res

    def s2c_register(self, s2c):
        """
        注册协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_login_host(self, s2c):
        """
        网关协议
        :param data: 
        :return: 
        """
        hosts = []
        hosts.append(s2c.code)
        hosts.append(s2c.ip)
        hosts.append(s2c.port)
        hosts.append(s2c.sign)
        return hosts

class S2C_ACHIEVE():

    def s2c_achieve_list(self, s2c):
        """
        获取成就列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.achieve_list)
        return res

    def s2c_get_achieve_reward(self, s2c):
        """
        领取成就奖励协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_update_achieve(self, data):
        """
        成就更新推送协议（后端主动发送的协议）
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.achieve)
        return res

class S2C_ARENA():

    def s2c_arena_camp(self, s2c):
        """
        竞技场布阵协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_arena_info(self, s2c):
        """
        获取竞技场信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.formation)
        res.append(s2c.rank)
        res.append(s2c.best_rank)
        res.append(s2c.reward_id_list)
        res.append(s2c.left_times)
        return res

    def s2c_get_arena_challenge_list(self, s2c):
        """
        刷新竞技场挑战对手信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.arena_player_list)
        return res

    def s2c_arena_challenge(self, s2c):
        """
        竞技场挑战对手协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_buy_arena_times(self, s2c):
        """
        竞技场购买挑战次数协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_arena_first_rank_reward(self, s2c):
        """
        竞技场领取首次达到排名奖励协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.reward_id)
        return res

    def s2c_get_arena_shop(self, s2c):
        """
        竞技场获取商店列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.info)
        return res

    def s2c_buy_arena_product(self, s2c):
        """
        竞技场购买商品协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_refresh_arena_shop(self, s2c):
        """
        竞技场刷新商品协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.info)
        return res

    def s2c_get_arena_log(self, s2c):
        """
        竞技场获取竞技场日志协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.log_list)
        return res

    def s2c_get_arena_rank(self, s2c):
        """
        获取竞技场排行榜信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.rank_player_list)
        res.append(s2c.total_page)
        res.append(s2c.now_page)
        res.append(s2c.update_time)
        return res

    def s2c_get_arena_player_info(self, s2c):
        """
        获取竞技场匹配玩家信息
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.arena_player_info)
        return res

class S2C_CHAT():

    def s2c_broadcast(self, s2c):
        """
        聊天协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.type)
        res.append(s2c.id)
        res.append(s2c.str)
        res.append(s2c.param)
        return res

class S2C_COMPOSE():

    def s2c_compose_partner(self, s2c):
        """
        伙伴合成协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.reward_partner_unique_id)
        return res

    def s2c_compose_trump(self, s2c):
        """
        法宝合成协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.goods_unique_id)
        return res

class S2C_DRAW():

    def s2c_draw(self, s2c):
        """
        抽卡协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.partner_unique_id_list)
        return res

class S2C_DUNGEON():

    def s2c_get_dungeon_info(self, s2c):
        """
        获取试炼信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.dungeons)
        return res

    def s2c_save_formation(self, s2c):
        """
        保存试炼副本进度协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_challenge(self, s2c):
        """
        试炼结果协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_dungeon_time(self, s2c):
        """
        获取时间协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.time)
        return res

class S2C_EXP_TRAIN():

    def s2c_get_exp_train_info(self, s2c):
        """
        获取练功房信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.double_time)
        res.append(s2c.train_info)
        return res

    def s2c_put_down(self, s2c):
        """
        练功房下阵协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_put_on(self, s2c):
        """
        练功房上阵协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_collect_train(self, s2c):
        """
        收获练功经验协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_gold_unlock(self, s2c):
        """
        元宝解锁练功栏协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_buy_double_time(self, s2c):
        """
        购买双倍经验协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

class S2C_FRIEND():

    def s2c_get_friend_list(self, s2c):
        """
        获取好友列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.friend_list)
        res.append(s2c.left_donate_times)
        res.append(s2c.receive_donate)
        return res

    def s2c_check_nickname_exists(self, s2c):
        """
        检测玩家存在协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_friend_apply(self, s2c):
        """
        申请好友协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_friend_apply_list(self, s2c):
        """
        获取好友申请列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.apply_list)
        return res

    def s2c_friend_apply_agree_reply(self, s2c):
        """
        同意好友申请协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.reply_list)
        return res

    def s2c_friend_apply_reject_reply(self, s2c):
        """
        拒绝或忽略好友申请协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.op)
        res.append(s2c.apply_id_list)
        return res

    def s2c_add_friend(self, s2c):
        """
        添加进好友列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.add_friend_list)
        return res

    def s2c_friend_del(self, s2c):
        """
        删除好友协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.friend_id)
        return res

    def s2c_friend_donate(self, s2c):
        """
        捐赠体力协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_refresh_donate_info(self, s2c):
        """
        刷新捐赠信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.left_donate_times)
        res.append(s2c.receive_donate)
        return res

    def s2c_refresh_donate_state(self, s2c):
        """
        刷新捐赠状态协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.friend_id)
        res.append(s2c.donate_state)
        return res

    def s2c_clear_friend_cache(self, s2c):
        """
        通知清除缓存列表协议(该协议无返回参数)
        :param data: 
        :return: 
        """
        res = []
        return res

class S2C_GOODS():

    def s2c_goods_list(self, s2c):
        """
        获取玩家物品列表协议
        :param data: 
        :return: [(物品ID，UID，数量),(物品ID，UID，数量)]
        """
        res = []
        s2cdict = pb2dict(s2c)
        if s2cdict:
            for each in s2cdict['goods_list']:
                goodid = int(each['goods_id'])
                uid = int(each['id'])
                num = int(each['num'])
                if 'main_attrs' in each and each['main_attrs']:
                    attr_type = int(each['main_attrs'][0]['attr_type'])
                    attr_value = int(each['main_attrs'][0]['attr_value'])
                else:
                    attr_type = None
                    attr_value = None
                res.append((goodid, uid, num, attr_type, attr_value))
        return res

    def s2c_update_goods_list(self, s2c):
        """
        更新物品列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.update_list)
        return res

    def s2c_delete_goods(self, s2c):
        """
        删除物品协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.del_id_list)
        return res

    def s2c_trump_up_lv(self, s2c):
        """
        法宝升级协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.old_lv)
        res.append(s2c.new_lv)
        res.append(s2c.old_vice_attrs)
        return res

    def s2c_trump_equip(self, s2c):
        """
        装备法宝协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trump_unequip(self, s2c):
        """
        装备法宝协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_goods_sell(self, s2c):
        """
        出售物品协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_goods_use(self, s2c):
        """
        使用物品协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

class S2C_GUDIE():

    def s2c_update_system_active(self, s2c):
        """
        激活系统消息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_update_guides(self, s2c):
        """
        提交引导信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_download_guide_info(self, s2c):
        """
        下载引导信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.actives)
        res.append(s2c.guide1)
        return res

class S2C_MAIL():

    def s2c_mail_list(self, s2c):
        """
        获取邮件列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.mails)
        return res

    def s2c_update_mail_list(self, s2c):
        """
        更新邮件列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.mails)
        return res

    def s2c_read_mail(self, s2c):
        """
        读取邮件协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_mail_rewards(self, s2c):
        """
        领取邮件附件协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.failed_mail_ids)
        return res

    def s2c_deleted_mail(self, s2c):
        """
        删除的邮件码获取协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.mail_id)
        return res

    def s2c_delete_mails(self, s2c):
        """
        删除邮件协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

class S2C_MAJOR():

    def s2c_get_major_list(self, s2c):
        """
        获取主角列表协议
        :param data: 
        :return: 
        """
        res = []
        s2cdict = pb2dict(s2c)
        if s2cdict:
            for each in s2cdict['major_list']:
                majorid = int(each['major_id'])
                res.append((majorid,))
        return res

    def s2c_major_switch(self, s2c):
        """
        主角切换协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_major_skill_switch(self, s2c):
        """
        技能切换协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_add_major(self, s2c):
        """
        新加/修改主角协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.major_info)
        return res

class S2C_MCITY():

    def s2c_get_mcity_info(self, s2c):
        """
        获取主城信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.avatar_id)
        res.append(s2c.avatar_list)
        res.append(s2c.can_rob)
        res.append(s2c.build_list)
        res.append(s2c.bag_goods_list)
        res.append(s2c.defence_info)
        res.append(s2c.rob_times)
        return res

    def s2c_get_mcity_build_info(self, s2c):
        """
        查看建筑信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.cur_production)
        res.append(s2c.last_production_time)
        return res

    def s2c_mcity_avatar(self, s2c):
        """
        装扮主城协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.avatar_id)
        return res

    def s2c_mcity_collect(self, s2c):
        """
        收取灵石/碎片协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.bag_goods_list)
        return res

    def s2c_mcity_set_defence(self, s2c):
        """
        设置防守协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.defence_info)
        return res

    def s2c_mcity_refresh_rob_times(self, s2c):
        """
        刷新玩家掠夺次数协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.rob_times)
        return res

    def s2c_mcity_buy_avatar(self, s2c):
        """
        购买装扮协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.avatar_id)
        return res

    def s2c_get_mcity_rob_list(self, s2c):
        """
        获取掠夺列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.rob_list)
        res.append(s2c.next_refresh_left_time)
        return res

    def s2c_mcity_refresh_rob_list(self, s2c):
        """
        刷新掠夺列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_other_mcity_info(self, s2c):
        """
        获取目标玩家主城信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.obj_player_id)
        res.append(s2c.obj_nickname)
        res.append(s2c.avatar_id)
        res.append(s2c.build_id_list)
        res.append(s2c.in_city)
        return res

    def s2c_mcity_rob(self, s2c):
        """
        掠夺协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.hero_list)
        res.append(s2c.obj_player_id)
        res.append(s2c.goods_id)
        res.append(s2c.goods_num)
        res.append(s2c.result)
        return res

    def s2c_mcity_rob_battle(self, s2c):
        """
        掠夺战斗协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.goods_id)
        res.append(s2c.goods_num)
        res.append(s2c.result)
        return res

    def s2c_mcity_revenge(self, s2c):
        """
        发起复仇协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.hero_list)
        res.append(s2c.goods_id)
        res.append(s2c.goods_num)
        res.append(s2c.result)
        return res

    def s2c_mcity_revenge_battle(self, s2c):
        """
        复仇战斗协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.goods_id)
        res.append(s2c.goods_num)
        res.append(s2c.result)
        return res

    def s2c_mcity_tip(self, s2c):
        """
        主城tips协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.type)
        return res

    def s2c_get_mcity_log_list(self, s2c):
        """
        获取主城日志列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.log_list)
        return res


class S2C_PARTNER():

    def s2c_get_partner_list(self, s2c):
        """
        获取伙伴列表协议
        :param data: 
        :return: 
        """
        res = []
        s2cdict = pb2dict(s2c)
        if s2cdict:
            for each in s2cdict['partner_list']:
                partnerid = int(each['partner_id'])
                UID = int(each['id'])
                star = int(each['star'])
                lv = int(each['lv'])
                res.append((partnerid, UID, star, lv))
        return res

    def s2c_partner_up_lv(self, s2c):
        """
        伙伴升级协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.old_lv)
        res.append(s2c.new_lv)
        return res

    def s2c_partner_up_star(self, s2c):
        """
        伙伴升星协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.old_star)
        res.append(s2c.new_star)
        return res

    def s2c_partner_wake(self, s2c):
        """
        伙伴觉醒协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_partner_switch_skin(self, s2c):
        """
        伙伴觉醒协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_partner_lock(self, s2c):
        """
        伙伴加锁协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_partner_change_notice(self, s2c):
        """
        刷新伙伴属性协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.id)
        res.append(s2c.attrs)
        return res

    def s2c_update_partner_notice(self, s2c):
        """
        新增/修改伙伴协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.partner_list)
        return res

    def s2c_update_partner_skill_notice(self, s2c):
        """
        伙伴技能修改协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.id)
        res.append(s2c.skills)
        return res

    def s2c_partner_add_skin(self, s2c):
        """
        伙伴新增皮肤协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.skin_id)
        return res

    def s2c_partner_del_ids(self, s2c):
        """
        伙伴删除协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.ids)
        return res

class S2C_PET():

    def s2c_get_pet_list(self, s2c):
        """
        获取灵宠列表协议
        :param data: 
        :return: 
        """
        res = []
        s2cdict = pb2dict(s2c)
        if s2cdict:
            for each in s2cdict['pet_list']:
                petid = int(each['pet_id'])
                uid = int(each['id'])
                lv = int(each['lv'])
                res.append((petid, uid, lv))
        return res

    def s2c_pet_switch(self, s2c):
        """
        切换灵宠协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_pet_up_lv(self, s2c):
        """
        升级灵宠协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_add_pet_notice(self, s2c):
        """
        获取灵宠通知协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.pet_info)
        return res

    def s2c_update_pet_lv_exp(self, s2c):
        """
        灵宠经验等级修改通知协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.id)
        res.append(s2c.lv)
        res.append(s2c.exp)
        return res

class S2C_PLAYER():

    def s2c_game_loaded(self, s2c):
        """
        玩家登录/重连游戏加载完成协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.is_wait)
        return res

    def s2c_get_player_info(self, s2c):
        """
        获取玩家信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.id)
        res.append(s2c.nickname)
        res.append(s2c.lingshi)
        res.append(s2c.gold)
        res.append(s2c.energy)
        res.append(s2c.major_id)
        res.append(s2c.lv)
        res.append(s2c.exp)
        res.append(s2c.pet_unique_id)
        res.append(s2c.major_skill_template_id)
        res.append(s2c.partner_skin_list)
        res.append(s2c.score_list)
        res.append(s2c.partner_id_list)
        res.append(s2c.spell)
        res.append(s2c.super_spell)
        return res

    def s2c_heart_check(self, s2c):
        """
        玩家登录/重连游戏加载完成协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.long_time)
        return res

    def s2c_update_score(self, s2c):
        """
        更新某种积分信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.score_info)
        return res

    def s2c_refresh_player_attr(self, s2c):
        """
        玩家属性更新协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.attrs)
        return res

    def s2c_reward_info(self, s2c):
        """
        玩家属性更新协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.rewards)
        res.append(s2c.reward_id)
        return res

    def s2c_five_refresh(self, s2c):
        """
        通知前端5点刷新协议
        :param data: 
        :return: 
        """
        return s2c

    def s2c_21_refresh(self, s2c):
        """
        通知前端21点刷新协议
        :param data: 
        :return: 
        """
        return s2c

    def s2c_red_tip(self, s2c):
        """
        红点提示协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.red_tip_list)
        return res

    def s2c_update_red_tip(self, s2c):
        """
        红点刷新协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.update_red_tip)
        return res

class S2C_PVE():

    def s2c_upload_pve(self, s2c):
        """
        上传pve进度协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_download_pve(self, s2c):
        """
        下载pve进度协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.main)
        res.append(s2c.branch1)
        res.append(s2c.branch2)
        res.append(s2c.branch3)
        res.append(s2c.branch4)
        print u"主线ID:" , res[0]
        return res

    def s2c_download_pve_state(self, s2c):
        """
        下载最新的场景状态协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.pos)
        res.append(s2c.list)
        return res

class S2C_PVP():

    def s2c_download_pve_state(self, s2c):
        """
        告诉玩家全局匹配成功，进入战斗协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_loading_progress(self, s2c):
        """
        告诉客户端加载进度协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_loading_complete(self, s2c):
        """
        告诉客户端玩家都加载完成协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_battle_info(self, s2c):
        """
        告诉玩家战斗信息协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_battle_command_result(self, s2c):
        """
        战斗指令发送结果协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_battle_command(self, s2c):
        """
        战斗指令服务器广播协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_state_change(self, s2c):
        """
        服务器状态切换通知客户端协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_state_now(self, s2c):
        """
        当前服务器状态协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_offline(self, s2c):
        """
        服务器通知客户端玩家离线协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_result(self, s2c):
        """
        服务器通知客户端玩家离线协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_reconnect_result(self, s2c):
        """
        服重连pvp服务的结果协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_online(self, s2c):
        """
        服务器通知客户端玩家上线协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_autofight(self, s2c):
        """
        自动战斗协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_record(self, s2c):
        """
        发送给玩家战斗录像协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_debug(self, s2c):
        """
        临时战斗消息协议
        :param data: 
        :return: 
        """
        res = []
        return res

class S2C_PVP_GOLOBAL():

    def s2c_pvp_global_join_result(self, s2c):
        """
        请求加入pvp等待协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_pvp_global_leav_result(self, s2c):
        """
        请求离开pvp等待结果协议
        :param data: 
        :return: 
        """
        res = []
        return res

class S2C_REALTIME_PVP():

    def s2c_get_realtime_pvp_state(self, s2c):
        """
        活动状态获取协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_get_realtime_pvp_info(self, s2c):
        """
        获取实时pvp信息协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_get_realtime_pvp_rank(self, s2c):
        """
        获取实时pvp排名协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_sign(self, s2c):
        """
        获取实时pvp标志协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_match(self, s2c):
        """
        实时pvp匹配协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_cancel_match(self, s2c):
        """
        取消实时pvp匹配协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_camp(self, s2c):
        """
        实时pvp部署协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_get_base_info(self, s2c):
        """
        获取实时pvp玩家信息协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_result(self, s2c):
        """
        实时pvp结算协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_realtime_pvp_match_over_time(self, s2c):
        """
        实时pvp匹配超时协议
        :param data: 
        :return: 
        """
        res = []
        return res

class S2C_SHOP():

    def s2c_get_products(self, s2c):
        """
        获取商品列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.version)
        for product in s2c.products:
            res.append(product.product_id)
            res.append(product.shop_id)
            res.append(product.page)
            res.append(product.rank)
            res.append(product.name)
            detail = product.detail
            for eachdetail in detail:
                res.append(eachdetail.type)
                res.append(eachdetail.id)
                res.append(eachdetail.num)
            res.append(product.cost)
            res.append(product.description)
            res.append(product.end_time)
            res.append(product.num_limit)
            res.append(product.quality)
            res.append(product.icon_path)
        return res

    def s2c_buy_product(self, s2c):
        """
        购买商品协议
        :param data: 
        :return: 
        """
        res = []
        return res

# 签到
class S2C_SIGN():

    def s2c_get_sign_info(self, s2c):
        """
        获取签到信息协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.day)
        res.append(s2c.is_sign)
        return res

    def s2c_sign(self, s2c):
        """
        签到协议
        :param data: 
        :return: 
        """
        res = []
        return res

# 任务
class S2C_TASK():

    def s2c_load_pve_task(self, s2c):
        """
        服务器返回剧情任务协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_get_daily_task_list(self, s2c):
        """
        获取日常任务列表协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_task_daily_reward(self, s2c):
        """
        日常任务领奖协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_task_secret_reward(self, s2c):
        """
        秘闻领奖协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_get_task_secret_reward(self, s2c):
        """
        获取秘闻奖励状态协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_get_story_branch(self, s2c):
        """
        获取支线剧情列表协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_update_story_list(self, s2c):
        """
        增量更新支线剧情列表协议
        :param data: 
        :return: 
        """
        res = []
        return res

    def s2c_update_story_data_list(self, s2c):
        """
        增量提交支线剧情数据协议
        :param data: 
        :return: 
        """
        res = []
        return res

# 试炼
class S2C_TRIAL():

    def s2c_trial_register(self, s2c):
        """
        报名参与试练副本协议
        :param data: 
        :return: 
        """
        res = []
        # res.append(s2c.code)
        # res.append(s2c.partner_unique_id_list)
        # event_list = s2c.event_list
        # for event in event_list:
        #     res.append(s2c.pos)
        #     res.append(s2c.event_type)
        #     res.append(s2c.kill_mon_list)
        #     res.append(s2c.is_finish)
        #     res.append(s2c.is_reward)
        # res.append(s2c.major_id)
        return res

    def s2c_trial_reconnect(self, s2c):
        """
        重连处理协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.floor)
        res.append(s2c.partner_unique_id_list)
        res.append(s2c.major_id)
        return res

    def s2c_trial_next_floor(self, s2c):
        """
        请求进入下一层协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.floor)
        return res

    def s2c_trial_open_box(self, s2c):
        """
        开启宝箱协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.add_score)
        res.append(s2c.is_seal)
        return res

    def s2c_trial_buji(self, s2c):
        """
        请求补给协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trial_jiachi(self, s2c):
        """
        触发加持协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trial_jiachi_select(self, s2c):
        """
        选择加持套装协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.buff_id)
        return res

    def s2c_trial_shop_list(self, s2c):
        """
        获取商人列表协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trial_shop_buy(self, s2c):
        """
        商人购买协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trial_open_jiejie(self, s2c):
        """
        打开神秘结界协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.event_index)
        res.append(s2c.add_score)
        res.append(s2c.buff_id)
        res.append(s2c.mon_id_list)
        return res

    def s2c_trial_battle(self, s2c):
        """
        杀完怪物调用协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.trial_id)
        res.append(s2c.pos)
        res.append(s2c.buff_id)
        return res

    def s2c_trial_exit(self, s2c):
        """
        结束试练结算协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_trial_reward(self, s2c):
        """
        刷新奖励协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.score)
        res.append(s2c.buff_id_list)
        res.append(s2c.score_explore)
        return res

    def s2c_trial_use_recover(self, s2c):
        """
        使用恢复药剂协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.reward_id)
        res.append(s2c.num)
        return res

# 秘境
class S2C_WONDERLAND():

    def s2c_wonderland_register(self, s2c):
        """
        报名参与秘境副本协议
        :param data: 
        :return: 
        """
        res = []
        # res.append(s2c.code)
        # res.append(s2c.opened_boxes)
        # res.append(s2c.pass_reward)
        return res

    def s2c_wonderland_pass(self, s2c):
        """
        领取通关奖励协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        res.append(s2c.wonderland_id)
        return res

    def s2c_wonderland_open_box(self, s2c):
        """
        打开密境中的宝箱协议
        :param data: 
        :return: 
        """
        res = []
        res.append(s2c.code)
        return res

    def s2c_get_wonderland_list(self, s2c):
        """
        获取秘境已经通关的列表协议
        :param data: 
        :return: 
        """
        res = []
        wonderland_list = s2c.wonderland_list
        for wonderland in wonderland_list:
            res.append(wonderland.wonderland_id)
            res.append(wonderland.opened_boxes)
            res.append(wonderland.pass_reward)
        return res


class S2C_RPC():

    pass


class S2C_PROTO(S2C_ACCNAME,S2C_ACHIEVE,S2C_ARENA,S2C_CHAT,S2C_COMPOSE,S2C_DRAW,S2C_DUNGEON,S2C_EXP_TRAIN,S2C_FRIEND,
                S2C_GOODS,S2C_GOODS,S2C_GUDIE,S2C_MAIL,S2C_MAJOR,S2C_MCITY,S2C_PARTNER,S2C_PET,S2C_PLAYER,S2C_PVE,
                S2C_PVP,S2C_PVP_GOLOBAL,S2C_REALTIME_PVP,S2C_SHOP,S2C_SIGN,S2C_TASK,S2C_TRIAL,S2C_WONDERLAND,S2C_RPC):
    """
    全继承包，集成所有协议超类中的解析方法
    """
    pass

