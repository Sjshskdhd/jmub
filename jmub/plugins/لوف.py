# PLUGIN MADE BY @RRRLz FOR @ZedThon
# 𝖹Ꭵᥣᴢᥲ️ᥣ

import random

from jmub import jmub
from jmub.core.managers import edit_or_reply
from jmub.helpers import get_user_from_event
from razan.strings.fun import *

from . import *


@jmub.ar_cmd(incoming="لوف ?(.*)")
async def _(event):
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       await event.edit(f"""{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t} 
             {t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n


{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n
⁭
           {t}{t}{t}{t}{t}
      {t}{t}{t}{t}{t}{t}{t}
   {t}{t}                       {t}{t}
 {t}{t}                          {t}{t}
{t}{t}                            {t}{t}
{t}{t}                            {t}{t}
 {t}{t}                           {t}{t}
   {t}{t}                       {t}{t}
       {t}{t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}{t}\n
⁭
{t}{t}                              {t}{t}
  {t}{t}                          {t}{t}
    {t}{t}                      {t}{t}
      {t}{t}                  {t}{t}
         {t}{t}             {t}{t}
           {t}{t}         {t}{t}
             {t}{t}     {t}{t}
               {t}{t} {t}{t}
                  {t}{t}{t}
                       {t}\n
⁭
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n

{t}{t}                         {t}{t}
  {t}{t}                    {t}{t}
     {t}{t}              {t}{t}
        {t}{t}        {t}{t}
           {t}{t}  {t}{t}
              {t}{t}{t}
                {t}{t}
                {t}{t}
                {t}{t}
                {t}{t}
                {t}{t}\n
⁭
        {t}{t}{t}{t}{t}{t}
     {t}{t}{t}{t}{t}{t}{t}
   {t}{t}                     {t}{t}
 {t}{t}                         {t}{t}
{t}{t}                           {t}{t}
{t}{t}                           {t}{t}
 {t}{t}                         {t}{t}
   {t}{t}                     {t}{t}
      {t}{t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}{t}\n
⁭
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
  {t}{t}                  {t}{t}
      {t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}""")
      

          
